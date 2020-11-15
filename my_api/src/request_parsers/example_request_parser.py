import logging

from ..exceptions import HouseKeepingBaseException
from .housekeeping_utilties import get_field
from .housekeeping_utilties import get_json

LOG = logging.getLogger(__name__)

class ExampleRequestParser:

    def parse(self, request):
        """
        Transforms a flask request into whatever the Controller needs.  In this case, it just returns
        the JSON request body, though the `get_field()` function can be used to extract required fields.
        """
        body = get_json(request)
        return body