# letsbuilda-pypi

A wrapper for [PyPI's API and RSS feeds](https://warehouse.pypa.io/api-reference/index.html).

## Usage

### Sync client

```py
from httpx import Client
from letsbuilda.pypi import PyPIServices

http_client = Client()
pypi_client = PyPIServices(http_client)

print(pypi_client.get_rss_feed(pypi_client.NEWEST_PACKAGES_FEED_URL))
print(pypi_client.get_package_metadata("letsbuilda-pypi"))
```

### Async client

```py
from httpx import AsyncClient
from letsbuilda.pypi.async_client import PyPIServices

http_client = AsyncClient()
pypi_client = PyPIServices(http_session)

print(await pypi_client.get_rss_feed(pypi_client.NEWEST_PACKAGES_FEED_URL))
print(await pypi_client.get_package_metadata("letsbuilda-pypi"))
```
