import os

import click
from rich import print as rich_print

from pychassiscli.utils import get_directory, status, copy_files, check_docker, generate_metric_config

from pychassiscli.utils import (start_metric_servers, stop_metric_servers, start_prometheus, start_statsd_exporter,
                   start_statsd_agent, start_grafana, start_metric_network, stop_metric_network, stop_grafana,
                   stop_prometheus, stop_statsd_exporter, stop_statsd_agent, refresh_metric_servers)

GENERATE_TYPE_CHOICES = ['apiflask', 'nameko', 'metrics', 'unit_test']
SERVICE_CHOICES = ['metrics', 'metrics_network', 'prometheus', 'grafana', 'statsd_exporter', 'statsd_agent']
REFRESH_SERVICE_CHOICES = ['metrics']

service_starting_dict = {
    'metrics': start_metric_servers,
    'metrics_network': start_metric_network,
    'grafana': start_grafana,
    'prometheus': start_prometheus,
    'statsd_exporter': start_statsd_exporter,
    'statsd_agent': start_statsd_agent,
}

service_stopping_dict = {
    'metrics': stop_metric_servers,
    'metrics_network': stop_metric_network,
    'grafana': stop_grafana,
    'prometheus': stop_prometheus,
    'statsd_exporter': stop_statsd_exporter,
    'statsd_agent': stop_statsd_agent,
}

service_refreshing_dict = {
    'metrics': refresh_metric_servers,
}


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--directory',
              default='.',
              show_default=True,
              help='The directory name for the template to be placed')
@click.option('-t', '--type', '_type',
              default='nameko',
              show_default=True,
              type=click.Choice(GENERATE_TYPE_CHOICES, case_sensitive=False),
              help='The types of the template')
@click.option('-m', '--module', 'nameko_module',
              required=False,
              help='The module name where the nameko service exists')
@click.option('-c', '--class', 'class_name_str',
              required=False,
              help='The class name of the nameko service')
def gen(directory, _type, nameko_module, class_name_str):
    """
    Generate a bunch of files of the project via templates.
    """
    if _type == 'metrics':
        if not nameko_module:
            # TODO input 让用户在命令行输入
            pass
        if not class_name_str:
            # TODO input 让用户在命令行输入
            pass
        generate_metric_config(nameko_module, class_name_str)
        return

    if _type == 'unit_test':
        if not os.access(directory, os.F_OK) or not os.listdir(directory):
            rich_print('Directory {} dose not exist or is empty'.format(directory))
            return

        tests_dir = os.path.join(get_directory('tests'), 'unit')
        if not os.access(tests_dir, os.F_OK):
            rich_print('No such test type {}'.format('unit'))
            return

        copy_files(tests_dir, directory)
    else:
        template_dir = os.path.join(get_directory('templates'), _type)
        if not os.access(template_dir, os.F_OK):
            rich_print('No such template type {}'.format(_type))
            return

        if directory != '.':
            if os.access(directory, os.F_OK) and os.listdir(directory):
                rich_print('Directory {} already exists and is not empty'.format(directory))
                return

            if not os.access(directory, os.F_OK):
                with status(f'Creating directory {os.path.abspath(directory)!r}'):
                    os.makedirs(directory)

        copy_files(template_dir, directory)


@cli.command()
@click.option('-s', '--service',
              required=True,
              type=click.Choice(SERVICE_CHOICES, case_sensitive=False),
              help='The name of service')
def start(service):
    """
    Start a service
    """
    check_docker()
    service_starting_dict.get(service)()


@cli.command()
@click.option('-s', '--service',
              required=True,
              type=click.Choice(SERVICE_CHOICES, case_sensitive=False),
              help='The name of service')
def stop(service):
    """
    Stop a service
    """
    check_docker()
    service_stopping_dict.get(service)()


@cli.command()
@click.option('-s', '--service',
              required=True,
              type=click.Choice(REFRESH_SERVICE_CHOICES, case_sensitive=False),
              help='The name of service')
def refresh(service):
    """
    Refresh a service
    """
    check_docker()
    service_refreshing_dict.get(service)()


if __name__ == '__main__':
    cli()
