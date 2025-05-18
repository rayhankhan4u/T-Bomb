"""
provider.py - API request handler for T-Bomb by Rayhan

This module manages API providers to send SMS, call, or email requests for the T-Bomb tool.
It loads API configurations from a local apidata.json file and handles threading for concurrent requests.

Developed by Rayhan for educational purposes.
"""

import threading
import requests
import json
import time


class APIProvider:
    """
    A class to manage API providers and send requests for SMS, call, or email bombing.
    """
    api_providers = []
    delay = 0
    status = True

    def __init__(self, cc, target, mode, delay=0):
        """
        Initialize the APIProvider with country code, target, mode, and delay.

        Args:
            cc (str): Country code (e.g., '91' for India).
            target (str): Target phone number or email.
            mode (str): Mode of operation ('sms', 'call', or 'mail').
            delay (float): Delay between requests in seconds.
        """
        try:
            PROVIDERS = json.load(open('apidata.json', 'r'))
        except Exception as e:
            raise FileNotFoundError(
                f"Failed to load apidata.json: {str(e)}. "
                "Ensure apidata.json exists in the project directory."
            )
        self.config = None
        self.cc = cc
        self.target = target
        self.mode = mode
        self.index = 0
        self.lock = threading.Lock()
        self.api_version = PROVIDERS.get("version", "3.0.0-rayhan")
        APIProvider.delay = delay
        providers = PROVIDERS.get(mode.lower(), {})
        APIProvider.api_providers = providers.get(cc, [])
        if len(APIProvider.api_providers) < 10:
            APIProvider.api_providers += providers.get("multi", [])

    def format(self):
        """
        Format the API configuration by replacing placeholders with target and country code.
        """
        config_dump = json.dumps(self.config)
        config_dump = config_dump.replace("{target}", self.target)
        config_dump = config_dump.replace("{cc}", self.cc)
        self.config = json.loads(config_dump)

    def select_api(self):
        """
        Select the next API provider from the list and prepare its configuration.
        """
        try:
            if len(APIProvider.api_providers) == 0:
                raise IndexError
            self.index += 1
            if self.index >= len(APIProvider.api_providers):
                self.index = 0
        except IndexError:
            self.index = -1
            return
        self.config = APIProvider.api_providers[self.index]
        perma_headers = {
            "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        }
        if "headers" in self.config:
            self.config["headers"].update(perma_headers)
        else:
            self.config["headers"] = perma_headers
        self.format()

    def remove(self):
        """
        Remove the current API provider from the list.

        Returns:
            bool: True if removal is successful, False otherwise.
        """
        try:
            del APIProvider.api_providers[self.index]
            return True
        except Exception:
            return False

    def request(self):
        """
        Send an HTTP request to the selected API provider.

        Returns:
            bool or None: True if the request is successful, False if it fails,
                          None if no valid API is available.
        """
        self.select_api()
        if not self.config or self.index == -1:
            return None
        identifier = self.config.pop("identifier", "").lower()
        del self.config['name']
        self.config['timeout'] = 30
        try:
            response = requests.request(**self.config)
            return identifier in response.text.lower()
        except Exception:
            return False

    def hit(self):
        """
        Execute an API request with threading lock and delay.

        Returns:
            bool or None: True if the request is successful, False if it fails,
                          None if no valid API is available.
        """
        try:
            if not APIProvider.status:
                return
            time.sleep(APIProvider.delay)
            self.lock.acquire()
            response = self.request()
            if response is False:
                self.remove()
            elif response is None:
                APIProvider.status = False
            return response
        except Exception:
            response = False
        finally:
            self.lock.release()
            return response
