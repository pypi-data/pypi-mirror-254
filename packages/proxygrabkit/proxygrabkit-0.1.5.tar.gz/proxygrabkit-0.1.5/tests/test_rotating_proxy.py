import logging
import os
import unittest

from dotenv import load_dotenv
from proxygrabkit import RotatingProxyClient

# LOAD SETTINGS
load_dotenv()
API_KEY = os.getenv("ROTATING_PROXY_API_KEY")

if API_KEY is None:
    raise Exception("API_KEY must ve provided.")

logging.basicConfig(filename=f"{__package__}.log")


def dict_isin( a: dict, b: dict ) -> bool:
    for k,v in a.items():
        if k not in b:
            return False
        if b[k] != v:
            return False
    
    return True


class TestRotatingProxy(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._filters = [
            {
                "get": True,  
                "referer": True,
                "country": "US",
            },
            {
                "get": True,  # Proxy supports GET requests
                "city": "New York",  # Return only proxies from New York City
            },
            {
                "get": True,  # Proxy supports GET requests
                "userAgent": True,
                "connectionType": 'Residential',  
            },
            {
                "get": True,  # Proxy supports GET requests
                "post": True,
            },
        ]

    def test_filters_assignment(self):
        '''Test that filters are assigned correctly.
        '''
        rotator = RotatingProxyClient(api_key=API_KEY)
        
        for f in self._filters:
            f_ret = rotator.set_filter( filter=f )
            self.assertTrue( dict_isin( f, f_ret ) )

    def test_remaining_requests(self):
        '''Test that the returned proxy it's compatible with filter
        '''
        rotator = RotatingProxyClient(api_key=API_KEY)
        self.assertIsNone( rotator.remaining_requests )
        
        rotator.get_proxy()
        
        self.assertIsNotNone( rotator.remaining_requests )


if __name__ == "__main__":
    unittest.main()
