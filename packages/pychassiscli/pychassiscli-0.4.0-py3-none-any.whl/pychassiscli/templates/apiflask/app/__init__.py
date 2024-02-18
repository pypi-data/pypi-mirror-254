from apiflask import APIFlask
from pychassislib.namekoproxy_pool import FlaskPooledServiceRpcProxy
from werkzeug.middleware.proxy_fix import ProxyFix

from app.config.config import Config
from app.util.common import basedir


rpc = FlaskPooledServiceRpcProxy()


def register_blueprints(apiflask_app):
    from app.api.v1 import create_v1

    apiflask_app.register_blueprint(create_v1(), url_prefix='/xxx/v1')


def load_app_config(app):
    """
    加载配置类到app config
    """
    app.config.from_object('app.config.config.Config')


def load_rpc_client(apiflask_app):
    apiflask_app.config.update(dict(
        NAMEKO_AMQP_URI=str(Config.RABBITMQ_URI)
    ))
    rpc.init_app(apiflask_app, extra_config={
        'INITIAL_CONNECTIONS': 2,
        'MAX_CONNECTIONS': 10,
        'POOL_RECYCLE': 1800  # 30 分钟后过期所有已有链接
    })


def set_security_schemes(app):
    app.security_schemes = {
        'AccessTokenAuth': {
            'type': 'AccessToken',
            'in': 'body',
            'name': 'access token',
        },
        'SessionAuth': {
            'type': 'Session',
            'in': 'header',
            'name': 'session',
        }
    }


def set_contact_info(app):
    app.contact = {
        'name': 'API Support',
        'url': '',
        'email': 'bryant@7-speed.com'
    }


def set_doc_ui_cdn(app):
    app.config['SWAGGER_UI_BUNDLE_JS'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.11.1/swagger-ui-bundle.min.js'
    app.config['SWAGGER_UI_CSS'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.11.1/swagger-ui.min.css'
    app.config['SWAGGER_UI_STANDALONE_PRESET_JS'] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.11.1/swagger-ui-standalone-preset.min.js'
    app.config['REDOC_STANDALONE_JS'] = 'https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js'


def create_app():
    app = APIFlask(__name__, title='Body Record API', version='1.0.0', docs_ui='redoc')
    app.servers = [
        {
            'name': 'Production Server',
            'url': 'https://www.bearcatlog.com/pzx/'
        }
    ]
    app = APIFlask(__name__, title='XXX API', version='1.0.0', docs_ui='redoc', docs_path='/xxx/docs',
                   spec_path='/xxx/openapi.json')
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    set_doc_ui_cdn(app)
    set_security_schemes(app)
    set_contact_info(app)
    load_app_config(app)
    register_blueprints(app)
    load_rpc_client(app)
    return app