# ProxyGrabKit

[![PyPI version](https://badge.fury.io/py/proxygrabkit.svg)](https://badge.fury.io/py/proxygrabkit)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A useful python package to obtain free proxies using several services.

## Description

Your Python package for retrieving internet proxy servers using free services.

### Features

- **GimmeProxy.com Integration**: Fetch proxies from GimmeProxy service.
- **ProxyRotator.com Integration**: Fetch proxies using the ProxyRotator API.

## Installation

You can install the package using pip:

```bash
pip install proxygrabkit
```

## Usage

### Fetching proxies from GimmeProxy.com

```py
from proxygrabkit import GimmeProxyClient

# Declare a object of type GimmeProxyClient
proxy_fetcher = GimmeProxyClient()

# Get a random proxy
proxy = proxy_fetcher.get_proxy()

print( proxy.proxy )
print( proxy.lastChecked )

```

### Fetching proxies from ProxyRotator.com

```py
from proxygrabkit import RotatingProxyClient

proxy_fetcher = RotatingProxyClient(api_key='xxxxxxxxxxxxxxxxxx')

proxy = proxy_fetcher.get_proxy()

print( proxy.proxy )
print( proxy.lastChecked )

```

## More examples

See examples folder for more complex examples

## Future Plans

- [ ] Support for <www.proxy-list.download>: Add functionality to retrieve proxies from this service.
- [ ] Support for <https://www.sslproxies.org/>: Incorporate support for SSL proxies from this source.
- [ ] Continuous Improvement and New Service Additions: Regularly update and add support for new proxy services.

## Contribution

If you encounter any issues or have enhancements to propose, feel free to open an issue or submit a pull request.

## License

This package is licensed under the MIT License. See the LICENSE file for details.
