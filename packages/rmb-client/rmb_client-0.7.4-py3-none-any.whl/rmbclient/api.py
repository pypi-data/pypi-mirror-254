import requests
from requests.exceptions import ConnectionError
from rmbclient.log import log
from rmbclient.exceptions import (
    ResourceExists,
    Unauthorized,
    ResourceNotFound,
    ServerInternalError,
    ServerConnectionError
)


class APIRequest:
    def __init__(self, api_url="http://127.0.0.1:5001",
                 token="", debug=False):
        self.api_url = api_url
        self.token = token
        self.debug = debug

    def _handle_request(self, method, url, headers, json=None, params=None):
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=json)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")
        return response

    def send(self, endpoint, method, data=None, params=None) -> dict or None:

        headers = {"Authorization": f"Bearer {self.token}"}
        url = f"{self.api_url}{endpoint}"

        try:
            response = self._handle_request(method, url, headers, json=data, params=params)
        except ConnectionError:
            raise ServerConnectionError(f"Server {url} Connection Error")

        if response.status_code in (200, 201):
            if method == 'DELETE':
                return True
            else:
                return response.json()

        try:
            _res = response.json()
        except Exception:
            _res = str(response)

        log_record = {'response': _res, 'method': method, 'endpoint': endpoint, 'data': data}

        if response.status_code == 409:
            raise ResourceExists("Resource already exists")
        elif response.status_code == 401:
            raise Unauthorized("Unauthorized")
        elif response.status_code in (404, 403):
            raise ResourceNotFound(f"Resource not found: {log_record}")
        elif response.status_code == 500:
            raise ServerInternalError(f"Server Internal Error: {log_record}")
        elif response.status_code == 400:
            raise ValueError(f"Bad Request: {log_record}")
        else:
            raise Exception(f"Error: {log_record}")


