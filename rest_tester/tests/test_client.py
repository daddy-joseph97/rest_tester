import os.path
import unittest

from rest_tester.client import ClientAPI


class ClientTestCase(unittest.TestCase):
    """Test case for the client methods using actual REST calls."""

    def setUp(self):
        self.client = ClientAPI()

    def tearDown(self):
        pass

    def test_user_request_collection(self):
        """Test for a single user from the entire collection.
        
        """
        username = 'readonly1'
        uri = 'http://localhost:6543/api/v0.1/users'
        response = self.client.request(uri=uri)
        #self.assertTrue('username' in d for d in response['users'])
        self.assertTrue({'username': username} in d.items() for d in response['users'])