
from typing import Any, Dict

from .proxy import ProxyData, ProxyFetcherAPI
from dataclasses import dataclass

@dataclass
class ProxyRP(ProxyData):
    '''Represent the information returned for a call to Rotating Proxy API

    Attributes:
     - connectionType (str): "Residential", "Mobile", or "Datacenter"
     - asn (str): ASN network
     - isp (str): Internet Service Provider
     - randomUserAgent (str): -----
     - requestsRemaining (int): Requests Remaining
    '''
    connectionType: str
    asn: str
    isp: str
    randomUserAgent: str

class RotatingProxyClient(ProxyFetcherAPI):
    """Class for interacting with the Rotating Proxy API from proxyrotator.com.

    Parameters
    ----------
    `api_key` : str
        The API key provided by proxyrotator.com for Rotating Proxy API.    
    
    Attributes
    ----------
    
    `api_key` : str
        The API key provided by proxyrotator.com for Rotating Proxy API.    
    `_API_BASE` : str
        The base URL of the API (constant).
    
    """

    _API_BASE = "http://falcon.proxyrotator.com:51337/"
    
    _VALID_PARAMS = [
        "apiKey",
        "get",
        "post",
        "cookies",
        "referer",
        "userAgent",
        "port",
        "city",
        "state",
        "country",
        "connectionType",
        "asn",
        "isp",
        "xml",
    ]

    def __init__(self, api_key: str) -> None:
        """Constructor of the RotatingProxy class.

        Parameters
        ----------
        `api_key` : str
            The API key provided by proxyrotator.com for Rotating Proxy API.    
        
        Example
        -------
        ```
            rotator = RotatingProxy( api_key = 'xxxxxxxxxxxx' )
        ```
        """
        super().__init__( RotatingProxyClient._API_BASE, RotatingProxyClient._VALID_PARAMS)
        self._api_key = api_key
        self._remaining_requests = None

    def set_filter(self, filter: Dict[str, Any] = {}, **kwargs) -> Dict[str, Any]:
        """ Sets filters for obtaining the proxy.

        Parameters
        ----------
        `filter`: dict
            A dict with the desired filters for the proxy.
        `**kwargs`:
            Filters indicated individually
        
        Note: Valid options for filter
        - 'get' (true): Proxy supports GET requests
        - 'post' (true): Proxy supports POST requests
        - 'cookies' (true): Proxy supports cookies
        - 'referer' (true): Proxy supports referer header
        - 'userAgent' (true): Proxy supports user-agent header
        - 'port' (integer): Return only proxies with specified port
        - 'city' (string): Return only proxies with specified city
        - 'state' (string): Return only proxies with specified state
        - 'country' (string): Return only proxies with specified country
        - 'connectionType' (string): "Residential", "Mobile", or "Datacenter"
        - 'asn' (string): Return only proxies on the specified ASN's network.
        - 'isp' (string): Return only proxies on the specified ISP's network.
            
        Return
        ------
        Dict[str, Any]
            A dict with the filters to be used
        
        Example 1
        ---------
        ```
        rotator = RotatingProxy( api_key = 'xxxxxxxxxxxx' )
        rotator.set_filter( filter = { 
                                'get': True, # Proxy supports GET requests 
                                'city': 'New York', # Return only proxies from New York City	
                                }
                            )
        
        ```

        Example 2
        ---------
        ```
        rotator = RotatingProxy( api_key = 'xxxxxxxxxxxx' )
        rotator.set_filter( get = True, # Proxy supports GET requests 
                            city = 'New York', # Return only proxies from New York City
                            )
        
        ```
        
        
        """
        self.clear_params()
        return self.set_params(filter, **kwargs)

    def get_proxy(self, filter: Dict[str, Any] = None) -> ProxyRP:
        """Gets a proxy from the API.

        Returns
        -------
        ProxyInfo
            The obtained proxy.
        
        Example
        -------
        ```
        rotator = RotatingProxy( api_key = 'xxxxxxxxxxxx' )
        rotator.set_filter( get = True, city = 'New York' )
                            
        proxy = rotator.get_proxy()             
        print( proxy.proxy )
        print( proxy.get )
        print( proxy.city )
        ``` 
        """
        
        if filter is not None:
            self.set_filter(filter=filter)
            
        self.set_params( apiKey = self._api_key )

        body = self._request_proxy( format='JSON' )
        
        if body is None:
            return None
        
        if 'error' in body:
            self._remaining_requests = 0
            error = body['error']
            raise RotatingProxyException( error )

        self._remaining_requests = body["requestsRemaining"]
        return ProxyRP(
            source = 'RotatingProxyAPI',
            proxy = body["proxy"],
            ip = body["ip"],
            port = body["port"],
            connectionType = body["connectionType"],
            asn = body["asn"],
            isp = body['isp'],
            type = body['type'],
            lastChecked = body['lastChecked'],
            get = body['get'],
            post = body['post'],
            cookies = body['cookies'],
            referer = body['referer'],
            userAgent = body['userAgent'],
            city = body['city'],
            state = body['state'],
            country = body['country'],
            randomUserAgent = body['randomUserAgent'],
            requestsRemaining = body['requestsRemaining']
        )


    @property
    def remaining_requests(self) -> 'int | None':
        '''Return the number of remaining requests.
        
        '''
        return self._remaining_requests
    
    @property
    def api_key(self):
        return self._api_key


class RotatingProxyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)        

    
