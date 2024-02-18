
from .proxy import ProxyFetcherAPI, ProxyData
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class ProxyGP(ProxyData):
    '''Represent the information returned for a call to GimmeProxy API

    Attributes (see Proxy class for more attributes):
        - 'supportsHttps'https support
        - 'protocol' (str): Proxy protocol
        - 'anonymityLevel' (int): Anonymity level, 1 - anonymous, 0 - not anonymous
        - 'websites' (dict): websites working through this proxy    
        - 'curl' (str): ready to use CURLOPT_PROXY option
        - 'type' (str): proxy protocol
        - 'speed' (int): proxy speed 
    '''
    supportsHttps: bool
    protocol: str
    anonymityLevel: int
    websites: dict
    curl: str
#    type: str -- check this
    speed: int

class GimmeProxyClient(ProxyFetcherAPI):
    """
    Use https://gimmeproxy.com/ api for get proxies.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(
            api_endpoint="https://gimmeproxy.com/api/getProxy",
            valid_params=[
                "get",
                "post",
                "cookies",
                "referer",
                "user-agent",
                "supportsHttps",
                "anonymityLevel",
                "protocol",
                "port",
                "country",
                "maxCheckPeriod",
                "websites",
                "minSpeed",
                "notCountry",
                "ipPort",
                "curl",
            ],
        )

        self._api_key = api_key
        if api_key is not None:
            self._params.update({"api_key": api_key})

    def set_filter(self, filter: Dict[str, Any] = {}, **kwargs) -> Dict[str, Any]:
        """
        Parameters
        ----------
        `filter`: dict
            A dict with the desired filters for the proxy.
        `**kwargs`:
            Filters indicated individually
        
        Note 1: Valid options for filter and **kwargs
        - 'get' (bool): Proxy supports GET requests
        - 'post' (bool): Proxy supports POST requests
        - 'cookies' (bool): Proxy supports cookies
        - 'referer' (bool): Proxy supports referer header
        - 'user-agent' or 'user_agent' (bool): Proxy supports user-agent header
        - 'supportsHttps' (bool): return only proxies with HTTPS support
        - 'anonymityLevel' (int): Anonymity level, 1 - anonymous, 0 - not anonymous
        - 'port' (integer): Return only proxies with specified port
        - 'country' (string): Return only proxies with specified country/countries
        - 'notCountry' (string): Exclude proxies from some country from search
        - 'minSpeed' (float [kb]): Return only proxies with speed more than specified in KB
        - 'maxCheckPeriod' (integer [seconds]): Return only proxies checked in last maxCheckPeriod seconds
        Note: See https://gimmeproxy.com/#api for more details
        """
        
        self.clear_params()
        
        # change name for user agent
        if "user_agent" in kwargs.keys():
            kwargs["user-agent"] = kwargs["user_agent"]
            kwargs.pop("user_agent")
            
        if "user_agent" in filter.keys():
            filter["user-agent"] = filter["user_agent"]
            filter.pop("user_agent")

        # include api_key
        if self._api_key is not None:
            kwargs.update({"api_key": self._api_key})
                
        return self.set_params(params=filter, **kwargs)


    def get_proxy(self) -> ProxyGP:
        
        body = self._request_proxy(format='JSON')
        
#        if response.status_code == 429 or response.content == "Rate limited.":
#            raise Exception("Rate limited.")
        if not isinstance(body, dict) :
            raise GimmeProxyException( body )
        
        return ProxyGP(
            source = 'Gimmeproxy API',
            proxy = body['ipPort'],
            ip = body['ip'],
            port = body['port'],
            type = 'unknown', #check
            lastChecked = body['verifiedSecondsAgo'],
            get = body['get'],
            post = body['post'],
            cookies = body['cookies'],
            referer = body['referer'],
            userAgent = body['user-agent'],
            city = 'unknown',
            state = 'unknown',
            country = body['country'],
            requestsRemaining = None,
            supportsHttps = body['supportsHttps'],
            protocol = body['protocol'],
            anonymityLevel = body['anonymityLevel'],
            websites = body['websites'],
            curl = body['curl'],
            speed = body['speed']
        )

class GimmeProxyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)        
