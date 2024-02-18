########################################################################################################################
# IMPORTS

import logging

import requests

########################################################################################################################
# CLASSES

logger = logging.getLogger(__name__)


class Nominatim:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def reverse(self, lat, lon):
        return requests.get(f"{self.endpoint}/reverse?lat={lat}&lon={lon}&format=json").json()


class NominatimInterface(Nominatim):
    def __init__(self, config):
        if "osm" in config:
            self.config = config["osm"]

            self.endpoint = self.config["nominatim_endpoint"]

        else:
            logger.warning("no osm section in config")

        super().__init__(self.endpoint)
