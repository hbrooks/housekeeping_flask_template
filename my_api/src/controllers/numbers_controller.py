from datetime import datetime
import logging
import json

from flask import Flask
from flask import g
from flask import jsonify
from flask import request
from flask import Blueprint

from ..request_parsers import ExampleRequestParser
from ..models import ExampleModel

LOG = logging.getLogger(__name__)

class NumbersController:

    blueprint = Blueprint(
            'numbers',
            __name__,
            url_prefix='/numbers')

    def __init__(self, request_parser: ExampleRequestParser, example_model: ExampleModel):
        self.request_parser = request_parser
        self.example_model = example_model

    def get_blueprint(self):
        @self.blueprint.route('/', methods=('POST',))
        def POST():
            return self._handle_POST()
        return self.blueprint

    def _handle_POST(self):
        """
        Returns all the same fields in the request body as well as a new field, n, which is a random number.
        """
        request_body = self.request_parser.parse(request)
        return {
            **request_body,
            'n': self.example_model.pick_random_number()
        }, 200
