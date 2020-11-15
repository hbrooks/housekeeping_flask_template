import json
import os
import logging

from flask import Flask
from flask_cors import CORS # TODO: Is this needed?

from flask import current_app
from flask import g

from .controllers import *
from .models import *
from .request_parsers import *
from .server_utilities import HouseKeepingApiServer
from .server_utilities import create_dict_from_env_vars
from .server_utilities import get_env_var

LOG = logging.getLogger(__name__)


class ApiOrchServerFactory: # TODO: Clean this up and move to shared package.
    def __init__(self):
        pass

    def create_housekeeping_server(self):
        self.models = self._create_models()
        self.request_parsers = self._create_request_parsers()
        self.controllers = self._create_controllers(self.models, self.request_parsers)

        blueprints = {
            self.controllers['numbers'].get_blueprint(),
        }

        return HouseKeepingApiServer(
            self.models,
            blueprints,
            build_app_context_function=self._build_app_context_function,
            before_request_function=self._before_request_function,
            health_check_function=self._health_check_function)

    def _create_models(self):
        example_model = ExampleModel()
        return {
            'example_model': example_model,
        }

    def _create_request_parsers(self):
        return {
            'numbers': ExampleRequestParser(),
        }

    def _create_controllers(self, models, request_parsers):
        return {
            'numbers': NumbersController(
                request_parsers['numbers'],
                models['example_model'],
            )
        }

    def _build_app_context_function(self):
        pass

    def _before_request_function(self):
        pass

    def _health_check_function(self):
        is_healthy = True
        try:
            pass
        except Exception as e:
            LOG.error(e)
            is_healthy = False
        if is_healthy: # TODO: Return app config.
            return '', 200
        else:
            return '', 500


def create_app():
    """
    Flask knows to call `create_app()`.
    """
    factory = ApiOrchServerFactory()
    hk_server = factory.create_housekeeping_server()
    print("Flask app created!")
    return hk_server.build_flask_app()


app = create_app()