import json
import pytest
from http import HTTPStatus
import os

# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal, assert_true, assert_dict_equal

# Local imports...
from tt_pip_package.tt_package import DB_API
from tt_pip_package.responses import User

class TestTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('tt_pip_package.tt_package.DB_API.get_users')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_getting_users_when_response_is_ok(self):
        # Configure the mock to return a response with an OK status code.
        self.mock_get.return_value.ok = True

        """
        with open('fake_db_info.json', 'r') as fake_db_data:
            fake_data = json.load(fake_db_data)
            users = fake_data
        """

        users = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            },
        ]
        
        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = users

        # Call the service, which will send a request to the ВІ.
        response = DB_API.get_users()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_list_equal(response.json(), users)

