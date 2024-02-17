# Dopt Blocks Python Library

[![pypi](https://img.shields.io/pypi/v/dopt-blocks-python-client.svg)](https://pypi.python.org/pypi/dopt-blocks-python-client)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install dopt-blocks-python-client
# or
poetry add dopt-blocks-python-client
```

## Usage

```python
from dopt.client import DoptApi

client = DoptApi(api_key="YOUR_API_KEY)

# Fetch a flow from dopt, including its blocks.  The first fetch of
# this (flow.sid, flow.version) tuple will initialize the flow for
# the `user_identifier`

flow = client.flows.get_flow(
    sid="example-flow",
    version=1,
    include="block",
    user_identifier="joe_mckenney",
    group_identifier=None,
)

print(flow)

# Fetch a block for some previously initialized flow
block = client.blocks.get_block(
    uid="9sKe7gx4HZj_VI7oxfVD3", version=1, user_identifier="joe_mckenney"
)

print(block)
```

## Async Client

```python
import asyncio
from dopt.client import AsyncDoptApi

async_client = AsyncDoptApi(api_key="YOUR_API_KEY)

async def get_flow() -> None:
    response = async_client.flows.get_flow(
      sid="example-flow",
      version=1,
      include="block",
      user_identifier="joe_mckenney",
      group_identifier=None,
    );
    print(response)

asyncio.run(get_flow())
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
