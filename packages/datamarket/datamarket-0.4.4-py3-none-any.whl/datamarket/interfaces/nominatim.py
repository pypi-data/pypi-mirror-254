########################################################################################################################
# IMPORTS

import logging

import requests

########################################################################################################################
# CLASSES

logger = logging.getLogger(__name__)


class NominatimInterface:
    def __init__(self, config):
        if "osm" in config:
            self.config = config["osm"]

            self.endpoint = self.config["endpoint"]

        else:
            logger.warning("no osm section in config")

    def reverse(self, lat, lon):
        return requests.get(f"{self.endpoint}/reverse?lat={lat}&lon={lon}&format=json").json()
