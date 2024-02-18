
import requests
from dataclasses import dataclass
from typing import Dict, Any
from requests import HTTPError
@dataclass
class ProxyData:
    """ Represent the information of one proxy

    Attributes:
        - source (str): Service used to get it.
        - proxy (str): proxy server
        - ip (str): server's ip
        - port (int): server's port
        - type (str): ---
        - lastChecked (int): Last check in seconds
        - get (bool): Proxy support GET requests
        - post (bool): Proxy support POST requests
        - cookies (bool): Proxy support cookies
        - referer (bool): Proxy support referer header
        - userAgent (bool): Proxy support user-agent header
        - city (str): City
        - state (str): State
        - country (str): Country

    """
    source: str
    proxy: str
    ip: str
    port: int
    type: str
    lastChecked: int
    get: bool
    post: bool
    cookies: bool
    referer: bool
    userAgent: bool
    city: str
    state: str
    country: str
    requestsRemaining: int


class ProxyFetcher(object):
    def __init__(self) -> None:
        pass
    
    def set_filter(self, **kwargs):
        raise Exception( 'This function must be implemented by classes that inherit from ProxyFetcher' )
 
    def get_proxy(self) -> ProxyData:
        raise Exception( 'This function must be implemented by classes that inherit from ProxyFetcher' )


class ProxyFetcherAPI(ProxyFetcher):
    def __init__(self, api_endpoint, valid_params) -> None:
        super().__init__()
        self._api_endpoint = api_endpoint
        self._valid_params = valid_params
        self._params = {}
	
    def clear_params(self):
        self._params.clear()
 
    def set_params(self, params: Dict[str, Any] = {}, **kwargs) -> dict:
        """
        Set params for api call

        :kwargs dictionary with params used for request.

        """
        for k, v in params.items():
            if k in self._valid_params:
                self._params.update({k: v})

        for k, v in kwargs.items():
            if k in self._valid_params:
                self._params.update({k: v})

        return self._params

    def _request_proxy(self, format :str = 'JSON' ) -> 'dict | str':
        try:
            response = requests.get(url=self._api_endpoint, params=self._params)
            response.raise_for_status()
            
        except HTTPError as e:
            print(f"{type(e).__name__}: {e}")
            
        except Exception as e:
            return f'{e}'

        if format == 'JSON':
            try:
                return response.json()
            except Exception:
                return str(response.text)
        else:
            return str(response.text)
            
