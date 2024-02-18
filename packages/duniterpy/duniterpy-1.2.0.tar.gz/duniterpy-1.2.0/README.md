# DuniterPy

Most complete client oriented Python library for [Duniter](https://git.duniter.org/nodes/typescript/duniter)/Ğ1 ecosystem.

This library was originally developed for [Sakia](https://git.duniter.org/clients/python/sakia) desktop client which is now discontinued.
It is currently used by following programs:

- [Tikka](https://git.duniter.org/clients/python/tikka), the desktop client.
- [Silkaj](https://silkaj.duniter.org/), command line client.
- [Jaklis](https://git.p2p.legal/axiom-team/jaklis), command line client for Cs+/Gchange pods.
- [Ğ1Dons](https://git.duniter.org/matograine/g1pourboire), Ğ1Dons, paper-wallet generator aimed at giving tips in Ğ1.

## Features

### Network

- APIs support: BMA, GVA, WS2P, and CS+:
  - [Basic Merkle API](https://git.duniter.org/nodes/typescript/duniter/-/blob/dev/doc/HTTP_API.md), first Duniter API to be deprecated
  - GraphQL Verification API, Duniter API in developement meant to replace BMA. Based on GraphQL.
  - Websocket to Peer, Duniter inter-nodes (servers) API
  - Cesium+, non-Duniter API, used to store profile data related to the blockchain as well as ads for Cesium and Ğchange.
- Non-threaded asynchronous/synchronous connections
- Support HTTP, HTTPS, and WebSocket transport for the APIs
- Endpoints management

### Blockchain

- Support [Duniter blockchain protocol](https://git.duniter.org/documents/rfcs#duniter-blockchain-protocol-dubp)
- Duniter documents management: transaction, block and WoT documents
- Multiple authentication methods
- Duniter signing key
- Sign/verify and encrypt/decrypt messages with Duniter credentials

## Requirements

- Python >= 3.8.0
- [graphql-core](https://pypi.org/project/graphql-core)
- [websocket-client](https://pypi.org/project/websocket-client)
- [jsonschema](https://pypi.org/project/jsonschema)
- [pyPEG2](https://pypi.org/project/pyPEG2)
- [base58](https://pypi.org/project/base58)
- [libnacl](https://pypi.org/project/libnacl)
- [pyaes](https://pypi.org/project/pyaes)
- [mnemonic](https://pypi.org/project/mnemonic)

## Installation

You will require following dependencies:

```bash
sudo apt install python3-pip python3-dev python3-wheel libsodium23
```

You can install DuniterPy and its dependencies with following command:

```sh
pip install --user duniterpy
```

Once you want to add DuniterPy to your Python project, you can add it as a dependency to your Python development environment: `pyproject.toml`, `requirements.txt`, `setup.py`.
We recommend [Poetry](https://python-poetry.org) usage.

## Documentation

[Online official automaticaly generated documentation](https://clients.pages.duniter.org/python/duniterpy/index.html)

## Examples

The [examples folder](https://git.duniter.org/clients/python/duniterpy/tree/master/examples) contains scripts to help you!

- Have a look at the `examples` folder
- Run examples from parent folder directly

```bash
python examples/request_data.py
```

Or from Python interpreter:

```bash
python
>>> import examples
# To list available examples
>>> help(examples)
# Run example
>>> examples.create_public_key()
```

`request_data_async` example requires to be run with `asyncio`:

```bash
>>> import examples, asyncio
>>> asyncio.get_event_loop().run_until_complete(examples.request_data_async())
```

## Contributing

- Checkout the [contributing guide](CONTRIBUTING.md).

## Packaging status

[![Packaging status](https://repology.org/badge/vertical-allrepos/python:duniterpy.svg)](https://repology.org/project/python:duniterpy/versions)
