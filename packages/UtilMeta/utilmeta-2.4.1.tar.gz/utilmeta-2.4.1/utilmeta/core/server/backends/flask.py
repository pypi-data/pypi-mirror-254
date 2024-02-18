import flask
from flask import Flask
from utilmeta.core.request.backends.werkzeug import WerkzeugRequestAdaptor
from utilmeta.core.response.backends.werkzeug import WerkzeugResponseAdaptor
from utilmeta.core.response import Response
from .base import ServerAdaptor
from utilmeta.core.api import API


class FlaskServerAdaptor(ServerAdaptor):
    backend = flask
    request_adaptor_cls = WerkzeugRequestAdaptor
    response_adaptor_cls = WerkzeugResponseAdaptor
    application_cls = Flask
    default_asynchronous = False
    HANDLED_METHODS = ("DELETE", "HEAD", "GET", "OPTIONS", "PATCH", "POST", "PUT")
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 5000

    def __init__(self, config):
        super().__init__(config)
        self.app = self.config._application or self.application_cls(self.config.module_name)
        self._ready = False

    def adapt(self, api: 'API', route: str, asynchronous: bool = None):
        if asynchronous is None:
            asynchronous = self.default_asynchronous
        self.add_api(self.app, api, asynchronous=asynchronous, route=route)

    def application(self):
        self.setup()
        return self.app

    def setup(self):
        if self._ready:
            return
        self.add_api(
            self.app,
            self.resolve(),
            asynchronous=self.asynchronous
        )

        # @self.app.after_server_start
        # async def startup(*_):
        #     await self.config.startup()
        #
        # @self.app.before_server_stop
        # async def shutdown(*_):
        #     await self.config.shutdown()

        self._ready = True

    def run(self, **kwargs):
        self.setup()
        self.config.startup()
        try:
            self.app.run(
                host=self.config.host or self.DEFAULT_HOST,
                port=self.config.port,
                debug=not self.config.production,
                **kwargs
            )
        finally:
            self.config.shutdown()

    def add_api(self, app: Flask, utilmeta_api_class, route: str = '', asynchronous: bool = False):
        """
        Mount a API class
        make sure it is called after all your fastapi route is set
        """
        from utilmeta.core.api.base import API
        if not issubclass(utilmeta_api_class, API):
            raise TypeError(f'Invalid api class: {utilmeta_api_class}')

        if route and route.strip('/'):
            route = '/' + route.strip('/')
            prepend = route + '/'
        else:
            prepend = route = '/'

        if asynchronous:
            @app.route(route, defaults={'path': ''}, methods=self.HANDLED_METHODS)
            @app.route('%s<path:path>' % prepend, methods=self.HANDLED_METHODS)
            async def f(path: str):
                from flask import request
                try:
                    path = self.load_route(path)
                    resp = await utilmeta_api_class(
                        self.request_adaptor_cls(request, path)
                    )()
                except Exception as e:
                    resp = getattr(utilmeta_api_class, 'response', Response)(error=e)
                return self.response_adaptor_cls.reconstruct(resp)
        else:
            @app.route(route, defaults={'path': ''}, methods=self.HANDLED_METHODS)
            @app.route('%s<path:path>' % prepend, methods=self.HANDLED_METHODS)
            def f(path: str):
                from flask import request
                try:
                    path = self.load_route(path)
                    resp = utilmeta_api_class(
                        self.request_adaptor_cls(request, path)
                    )()
                except Exception as e:
                    resp = getattr(utilmeta_api_class, 'response', Response)(error=e)
                return self.response_adaptor_cls.reconstruct(resp)
