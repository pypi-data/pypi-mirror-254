import json

from nameko import config
from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc, ServiceRpc
from nameko.timer import timer
from nameko.web.handlers import http
from werkzeug.wrappers import Response
from nameko_tracer import Tracer
from pychassislib import init_sentry, init_statsd


class HttpDemoService:

    name = "http_demo_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @http("GET", "/broken")
    @statsd.timer('broken')
    def broken(self, request):
        raise ConnectionRefusedError()

    @http('GET', '/books/<string:uuid>')
    @statsd.timer('demo_get')
    def demo_get(self, request, uuid):
        data = {'id': uuid, 'title': 'The unbearable lightness of being',
                'author': 'Milan Kundera'}
        return Response(json.dumps({'book': data}),
                        mimetype='application/json')

    @http('POST', '/books')
    @statsd.timer('demo_post')
    def demo_post(self, request):
        return Response(json.dumps({'book': request.data.decode()}),
                        mimetype='application/json')


class RpcResponderDemoService:

    name = "rpc_responder_demo_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @rpc
    @statsd.timer('hello')
    def hello(self, name):
        return "Hello, {}!".format(name)


class RpcCallerDemoService:

    name = "rpc_caller_demo_service"

    remote = ServiceRpc("rpc_responder_demo_service")

    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @rpc
    @statsd.timer('remote_hello')
    def remote_hello(self, value="John Doe"):
        res = u"{}".format(value)
        return self.remote.hello(res)


class EventPublisherService:

    name = "publisher_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    dispatch = EventDispatcher()

    @rpc
    @statsd.timer('publish')
    def publish(self, event_type, payload):
        self.dispatch(event_type, payload)


class AnEventListenerService:

    name = "an_event_listener_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @event_handler("publisher_service", "an_event")
    @statsd.timer('consume_an_event')
    def consume_an_event(self, payload):
        print("service {} received:".format(self.name), payload)


class AnotherEventListenerService:

    name = "another_event_listener_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @event_handler("publisher_service", "another_event")
    @statsd.timer('consume_another_event')
    def consume_another_event(self, payload):
        print("service {} received:".format(self.name), payload)


class ListenBothEventsService:

    name = "listen_both_events_service"

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @event_handler("publisher_service", "an_event")
    @statsd.timer('consume_an_event')
    def consume_an_event(self, payload):
        print("service {} received:".format(self.name), payload)

    @event_handler("publisher_service", "another_event")
    @statsd.timer('consume_another_event')
    def consume_another_event(self, payload):
        print("service {} received:".format(self.name), payload)


class Timer:

    name = 'timer'

    tracer = Tracer()
    sentry = init_sentry()
    statsd = init_statsd(config.get('STATSD_PREFIX'), config.get('STATSD_HOST'))

    @timer(interval=1)
    @statsd.timer('ping')
    def ping(self):
        # method executed every second
        print("pong")
