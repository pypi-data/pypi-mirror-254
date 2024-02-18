import os
import shutil
from time import sleep
from contextlib import contextmanager

from mako.template import Template
from rich import print as rich_print
from python_on_whales import DockerException, ClientNotFoundError, DockerClient


docker = DockerClient()


def check_docker():
    """
    Check if docker and docker compose are installed and running.
    """
    try:
        docker.ps()
    except ClientNotFoundError:
        rich_print('Please install docker firstly')
        raise
    except DockerException:
        rich_print('Please start docker correctly')
        raise

    rich_print('Good! [bold magenta]Docker is installed already[/bold magenta]', ":vampire:")

    # if not docker.compose.is_installed():
    #     rich_print('Please install docker compose firstly')
    #     raise
    #
    # rich_print('Good! [bold magenta]Docker Compose is installed already[/bold magenta]', ":vampire:")


@contextmanager
def status(status_msg: str, newline: bool = False, quiet: bool = False):
    """
    Show status message and yield.
    """
    msg_suffix = ' ...' if not newline else ' ...\n'
    rich_print(status_msg + msg_suffix)
    try:
        yield
    except Exception as e:
        if not quiet:
            rich_print('  [bold magenta]FAILED[/bold magenta]\n')
        raise
    else:
        if not quiet:
            rich_print('  [bold magenta]Done[/bold magenta]\n')


def get_directory(dir_name: str) -> str:
    """
    Return the directory path of the given pychassiscli directory name.
    """
    import pychassiscli

    package_dir = os.path.abspath(os.path.dirname(pychassiscli.__file__))
    return os.path.join(package_dir, dir_name)


def copy_files(src_dir, dest_dir):
    for file_ in os.listdir(src_dir):
        if file_ == '__pycache__':
            continue

        src_file_path = os.path.join(src_dir, file_)
        output_file = os.path.join(dest_dir, file_)
        if os.path.isdir(src_file_path):
            if not os.access(output_file, os.F_OK):
                with status(f'Creating directory {os.path.abspath(output_file)!r}'):
                    os.makedirs(output_file)
            copy_files(src_file_path, output_file)
        else:
            with status(f'Generating {os.path.abspath(output_file)}'):
                shutil.copy(src_file_path, output_file)


def template_to_file(
        template_file: str, dest: str, output_encoding: str, **kw
) -> None:
    template = Template(filename=template_file)
    try:
        output = template.render_unicode(**kw).encode(output_encoding)
    except Exception as e:
        rich_print('Template rendering failed.')
        raise
    else:
        with open(dest, "wb") as f:
            f.write(output)


def generate_metric_config(nameko_module, class_name_str):
    import sys
    import inspect
    import uuid
    sys.path.append(os.getcwd())
    for root, dirs, files in os.walk(os.getcwd()):
        for _dir in dirs:
            sys.path.append(os.path.join(root, _dir))

    # Extract information of statsd config from the class of nameko service
    file_name = nameko_module.split('.')[-1]
    _module = __import__(nameko_module)

    config_list = []
    for class_name in class_name_str.split(','):
        members = inspect.getmembers(getattr(getattr(_module, file_name), class_name), predicate=inspect.isfunction)
        for member_tuple in members:
            name, _obj = member_tuple
            unwrap = inspect.getclosurevars(_obj)
            if unwrap.nonlocals.get('self') and getattr(unwrap.nonlocals['self'], 'client'):
                statsd_prefix = unwrap.nonlocals['self'].client._prefix
                stat_name = unwrap.nonlocals['self'].stat
                config_list.append({
                    'statsd_prefix': statsd_prefix,
                    'stat_name': stat_name,
                    'class_name': class_name
                })

    # Generate one file of statsd config yaml for statsd exporter
    with status(f'Creating statsd_mapping.yml'):
        metric_configs_dir = os.path.join(get_directory('templates'), 'metric-configs')
        template_file_path = os.path.join(metric_configs_dir, 'statsd_mapping.yml.mako')
        output_file = os.path.join('.', f'statsd_mapping.yml')
        template_to_file(template_file=template_file_path, dest=output_file, output_encoding='utf-8',
                         **{'config_list': config_list})

    # Generate files of json for grafana dashboard
    if not os.access('grafana_dashboards', os.F_OK):
        with status(f'Creating directory {os.path.abspath("grafana_dashboards")!r}'):
            os.makedirs('grafana_dashboards')

    with status(f'Creating files of Grafana.json into the directory of grafana_dashboards'):
        for class_name in class_name_str.split(','):
            grafana_list = []
            for config in config_list:
                if config['class_name'] == class_name:
                    grafana_list.append(config)
            for idx, grafana_dict in enumerate(grafana_list):
                if idx + 1 == len(grafana_list):
                    grafana_dict['is_last'] = 1
                else:
                    grafana_dict['is_last'] = 0
            grafana_configs_dir = os.path.join(get_directory('templates'), 'metric-configs')
            grafana_file_path = os.path.join(grafana_configs_dir, 'grafana.json.mako')
            output_file = os.path.join('grafana_dashboards', f'{class_name}_Grafana.json')
            template_to_file(template_file=grafana_file_path, dest=output_file, output_encoding='utf-8',
                             **{'service_name': class_name, 'uid': uuid.uuid4(),
                                'grafana_list': grafana_list})


def start_network(network_name):
    with status(f'Starting network {network_name}'):
        docker.network.create(network_name, driver='bridge')


def stop_network(network_name):
    with status(f'Stopping network {network_name}'):
        docker.network.remove(network_name)


def start_metric_network():
    start_network('metric_servers')


def stop_metric_network():
    stop_network('metric_servers')


def start_statsd_agent():
    with status(f'Starting statsd agent'):
        metric_configs_dir = os.path.join(get_directory('templates'), 'metric-configs')
        statsd_config_file_path = os.path.join(metric_configs_dir, 'statsd_config.js')
        returned_string = docker.run(image='statsd/statsd:latest', name='statsd-agent', hostname='statsd-agent',
                                     detach=True, restart='always', interactive=True, tty=True,
                                     publish=[(8125, 8125, 'udp'), (8126, 8126)], pull='missing',
                                     volumes=[(statsd_config_file_path, '/usr/src/app/config.js', 'rw')],
                                     networks=['metric_servers'])
        rich_print('\nContainer ID: ' + '[bold magenta]' + str(returned_string) + '[/bold magenta]' + '\n')


def start_statsd_exporter():
    with status(f'Starting statsd exporter'):
        statsd_mapping_file_path = os.getcwd() + '/statsd_mapping.yml'
        returned_string = docker.run(image='prom/statsd-exporter:latest', name='statsd-exporter', pull='missing',
                                     detach=True, restart='always', tty=True, hostname='statsd-exporter',
                                     publish=[(9125, 9125, 'udp'), (9102, 9102)], interactive=True,
                                     command=['--statsd.mapping-config=/tmp/statsd_mapping.yml'],
                                     volumes=[(statsd_mapping_file_path, '/tmp/statsd_mapping.yml', 'rw')],
                                     networks=['metric_servers'])
        rich_print('\nContainer ID: ' + '[bold magenta]' + str(returned_string) + '[/bold magenta]' + '\n')


def start_prometheus():
    with status(f'Starting prometheus'):
        prometheus_conf_dir = os.path.join(get_directory('templates'), 'metric-configs')
        prometheus_conf_file_path = os.path.join(prometheus_conf_dir, 'prometheus_conf/prometheus.yml')
        returned_string = docker.run(image='prom/prometheus:latest', name='prometheus', hostname='prometheus',
                                     detach=True, restart='always', tty=True, interactive=True,
                                     publish=[(9193, 9090)], pull='missing',
                                     volumes=[(prometheus_conf_file_path, '/etc/prometheus/prometheus.yml', 'rw')],
                                     networks=['metric_servers'])
        rich_print('\nContainer ID: ' + '[bold magenta]' + str(returned_string) + '[/bold magenta]' + '\n')


def start_grafana():
    with status(f'Starting grafana'):
        grafana_conf_dir = os.path.join(get_directory('templates'), 'metric-configs')
        grafana_provisioning_path = os.path.join(grafana_conf_dir, 'grafana_conf/provisioning')
        grafana_config_path = os.path.join(grafana_conf_dir, 'grafana_conf/config/grafana.ini')
        grafana_dashboard_path = os.path.join(os.getcwd(), 'grafana_dashboards')
        returned_string = docker.run(image='grafana/grafana:latest', name='grafana', hostname='grafana',
                                     detach=True, restart='always', tty=True, interactive=True,
                                     publish=[(3100, 3000)], pull='missing',
                                     volumes=[(grafana_provisioning_path, '/etc/grafana/provisioning', 'rw'),
                                              (grafana_config_path, '/etc/grafana/grafana.ini', 'rw'),
                                              (grafana_dashboard_path, '/var/lib/grafana/dashboards', 'rw')],
                                     networks=['metric_servers'])
        rich_print('\nContainer ID: ' + '[bold magenta]' + str(returned_string) + '[/bold magenta]' + '\n')


def start_metric_servers():
    # TODO 检查相应容器是否已启动，如果启动，则先删除
    start_network('metric_servers')
    sleep(0.25)
    start_prometheus()
    sleep(0.25)
    start_statsd_exporter()
    sleep(0.25)
    start_statsd_agent()
    sleep(0.25)
    start_grafana()


def stop_statsd_agent():
    with status(f'Stopping statsd agent'):
        docker.remove('statsd-agent', force=True)
        rich_print('\nContainer is [bold magenta]removed[/bold magenta].' + '\n')


def stop_statsd_exporter():
    with status(f'Stopping statsd exporter'):
        docker.remove('statsd-exporter', force=True)
        rich_print('\nContainer is removed.' + '\n')


def stop_prometheus():
    with status(f'Stopping prometheus'):
        docker.remove('prometheus', force=True)
        rich_print('\nContainer is removed.' + '\n')


def stop_grafana():
    with status(f'Stopping grafana'):
        docker.remove('grafana', force=True)
        rich_print('\nContainer is removed.' + '\n')


def stop_metric_servers():
    stop_statsd_agent()
    sleep(0.25)
    stop_statsd_exporter()
    sleep(0.25)
    stop_prometheus()
    sleep(0.25)
    stop_grafana()
    sleep(0.25)
    stop_network('metric_servers')


def refresh_metric_servers():
    stop_statsd_exporter()
    sleep(0.25)
    stop_grafana()
    sleep(0.25)
    start_statsd_exporter()
    sleep(0.25)
    start_grafana()


if __name__ == '__main__':
    with status(f'Generating Test'):
        pass