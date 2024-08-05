import requests

from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from requests.exceptions import HTTPError, Timeout, RequestException
from .forms import AddressForm
from .utils import handle_api_errors


class AddressSearchTests(TestCase):
    def setUp(self):
        self.url = reverse('core:search')
    
    def test_address_length(self):
        """
        Test search view with an invalid address length
        """
        # invalid length
        data = {'address': '0x123'}

        with self.assertRaises(ValidationError):
            # make a POST request
            self.client.post(self.url, data=data)
    
    def test_address_prefix(self):
        """
        Test search view with an invalid address prefix
        """
        # invalid prefix
        data = {'address': '001234567890123456789012345678901234567890'}

        with self.assertRaises(ValidationError):
            # make a POST request
            self.client.post(self.url, data=data)

    def test_address_hexadecimal(self):
        """
        Test search view with an invalid address containing non-hexadecimal value
        """
        # invalid hexadecimal value
        data = {'address': '0x123456789012345678901234567890123456789z'}

        with self.assertRaises(ValidationError):
            # make a POST request
            self.client.post(self.url, data=data)


class ApiCallTests(TestCase):
    def test_http_error(self):
        url = 'https://httpbin.org/status/404'
        with self.assertRaises(HTTPError):
            handle_api_errors(url)
    

    def test_timeout_error(self):
        url = 'https://httpbin.org/delay/15'
        with self.assertRaises(Timeout):
            handle_api_errors(url)
    
    
    def test_connection_error(self):
        url = 'http://10.255.255.1'  # Non-routable IP address
        with self.assertRaises(RequestException):
            handle_api_errors(url)
