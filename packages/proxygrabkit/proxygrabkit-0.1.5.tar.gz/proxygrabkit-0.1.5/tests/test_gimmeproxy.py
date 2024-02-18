import os
import unittest

from dotenv import load_dotenv
from proxygrabkit import GimmeProxyClient


# LOAD SETTINGS
load_dotenv()
API_KEY = os.getenv("GIMME_PROXY_API_KEY", None)

def dict_isin( a: dict, b: dict ) -> bool:
    for k,v in a.items():
        if k not in b:
            return False
        if b[k] != v:
            return False
    
    return True


class TestGimmeProxy(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._filters = [
            {
                "get": True,  
                "referer": True,
            },
            {
                "get": True,  # Proxy supports GET requests
                "user-agent": True,
            },
            {
                "get": True,  # Proxy supports GET requests
                "post": True,
            },
            {
                "get": True,  # Proxy supports GET requests
                "post": True,
                "supportsHttps": True,
            },
        ]

    def test_filters_assignment(self):
        '''Test that filters are assigned correctly.
        '''
        proxy_fetcher = GimmeProxyClient(api_key=API_KEY)
        
        for f in self._filters:
            f_ret = proxy_fetcher.set_filter( filter=f, maxCheckPeriod=60*60*24 )
            self.assertTrue( dict_isin( f, f_ret )  )
            self.assertEqual( f_ret['maxCheckPeriod'], 60*60*24 )            

    def test_get_proxy(self):
        proxy_fetcher = GimmeProxyClient(api_key=API_KEY)
        
        proxy_fetcher.set_filter( get = True, supportsHttps=True )
        
        proxy = proxy_fetcher.get_proxy()
        
        self.assertEqual( proxy.source, 'Gimmeproxy API' )
        self.assertTrue( proxy.get )
        self.assertTrue( proxy.supportsHttps )

        

if __name__ == '__main__':
    unittest.main()