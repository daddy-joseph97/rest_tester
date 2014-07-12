import json
from urllib2 import urlopen

import requests
from requests.auth import HTTPBasicAuth


class ClientAPI(object):
    def request(self, uri, resource=None, params=None, body=None,
                headers=None, auth_creds=None):
        if auth_creds is not None:
            from requests.auth import HTTPBasicAuth
            auth = HTTPBasicAuth(username=auth_creds['username'],
                                 password=auth_creds['password'])
        else:
            auth = None
            
        response = requests.get(url=uri, params=params, auth=auth,
                                data=body, headers=headers)

        try:
            response_data = response.json()
        except ValueError:
            return {}
        
        return response_data