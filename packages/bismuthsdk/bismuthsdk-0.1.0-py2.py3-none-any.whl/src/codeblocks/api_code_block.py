from flask import Flask, request
from flask_restx import Api, Resource
from .auth_code_block import AuthCodeBlock
from .base_code_block import BaseCodeBlock


class APICodeBlock(BaseCodeBlock):
    def __init__(
        self,
        title="API",
        version="1.0",
        description="A simple API",
        app_config={},
        auth_code_block: AuthCodeBlock = None,
    ):
        self.app = Flask(__name__)
        self.app.config.update(app_config)
        self.api = Api(self.app, version=version, title=title, description=description)
        self.auth_code_block = auth_code_block

        super()

    def _auth_handler(self, method, handlers, require_auth, **kwargs):
        if method.lower() in map(lambda x: x.lower(), require_auth):
            return self.auth_code_block.token_required(handlers[method](**kwargs))
        else:
            return handlers[method](**kwargs)

    def add_route(
        self, route, methods, handlers, require_auth=["POST", "DELETE", "PUT"]
    ):
        methods = methods if isinstance(methods, list) else [methods]
        auth_handler = self._auth_handler

        class DynamicResource(Resource):
            def get(self, **kwargs):
                if "GET" in methods:
                    return auth_handler("GET", handlers, require_auth, **kwargs)
                else:
                    self.api.abort(404)

            def post(self, **kwargs):
                if "POST" in methods:
                    return auth_handler("POST", handlers, require_auth, **kwargs)
                else:
                    self.api.abort(404)

            def put(self, **kwargs):
                if "PUT" in methods:
                    return auth_handler("PUT", handlers, require_auth, **kwargs)
                else:
                    self.api.abort(404)

            def delete(self, **kwargs):
                if "DELETE" in methods:
                    return auth_handler("DELETE", handlers, require_auth, **kwargs)
                else:
                    self.api.abort(404)

        self.api.add_resource(DynamicResource, route)

    def run(self, host="0.0.0.0", port=5000, debug=False):
        self.app.run(host=host, port=port, debug=debug)
