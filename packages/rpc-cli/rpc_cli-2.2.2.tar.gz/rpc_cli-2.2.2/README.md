# RPC to CLI

![](https://img.shields.io/badge/License-ApacheV2-blue.svg)
![](https://img.shields.io/badge/code%20style-black-000000.svg)
![](https://img.shields.io/pypi/v/rpc-cli.svg)

Wrapper for [Python OpenRPC](https://python-openrpc.burkard.cloud/) to expose the
methods of an RPC Server through a CLI.

## Install

RPC CLI is on PyPI and can be installed with:

```shell
pip install rpc-cli
```

Or with [Poetry](https://python-poetry.org/)

```shell
poetry add rpc-cli
```

## Example

Given the following in a file `demo.py`.

```python
from openrpc import RPCServer
from pydantic import BaseModel

from rpc_cli import cli

rpc = RPCServer()


class Vector3(BaseModel):
    x: float
    y: float
    z: float


@rpc.method()
def get_distance(a: Vector3, b: Vector3) -> Vector3:
    """Get distance between two points."""
    return Vector3(x=a.x - b.x, y=a.y - b.y, z=a.z - b.z)


@rpc.method()
def divide(a: int, b: int) -> float:
    """Divide two integers."""
    return a / b


@rpc.method()
def summation(numbers: list[int | float]) -> int | float:
    """Summ all numbers in a list."""
    return sum(numbers)


if __name__ == "__main__":
    cli(rpc).run()
```

You now have a CLI.

![Demo](https://gitlab.com/mburkard/rpc-cli/-/raw/main/docs/demo.png)

### Using the CLI

Methods can be called as such, notice arrays and object parameters are passed as JSON
strings.

```shell
python demo.py get_distance '{"x": 1, "y": 1, "z": 1}' '{"x": 1, "y": 1, "z": 1}'
python demo.py divide 6 2
python demo.py summation '[1, 2, 3]'
```

## Auto Completions

This library uses [cleo](https://github.com/python-poetry/cleo), auto completions can be
made by following the instructions in the
[cleo docs](https://cleo.readthedocs.io/en/latest/introduction.html#autocompletion).

## Support The Developer

<a href="https://www.buymeacoffee.com/mburkard" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png"
       width="217"
       height="60"
       alt="Buy Me A Coffee">
</a>
