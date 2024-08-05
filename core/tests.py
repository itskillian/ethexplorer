import requests

from django.test import TestCase
from requests.exceptions import HTTPError, Timeout, RequestException
from .utils import handle_api_errors

class ApiCallTests(TestCase):
    def test_http_error(self):
        url = 'https://httpbin.org/status/404'
        result = handle_api_errors(url)
        self.assertIsInstance(result, HTTPError)
    

    def test_timeout_error(self):
        url = 'https://httpbin.org/delay/15'
        result = handle_api_errors(url)
        self.assertIsInstance(result, Timeout)
    
    
    def test_connection_error(self):
        url = 'http://10.255.255.1'  # Non-routable IP address
        result = handle_api_errors(url)
        self.assertIsInstance(result, RequestException)
