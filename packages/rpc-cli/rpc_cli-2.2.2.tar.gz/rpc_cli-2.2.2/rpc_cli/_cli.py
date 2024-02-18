"""Expose Python OpenRPC methods to a CLI."""
import asyncio
import json
import re
from typing import Any, Callable

from cleo.application import Application
from cleo.commands.command import Command
from cleo.helpers import argument
from openrpc import (
    ContentDescriptor,
    Method,
    OpenRPC,
    ParamStructure,
    RPCServer,
    Schema,
)


def cli(rpc: RPCServer, *, exclude_discover: bool = False) -> Application:
    """Generate a CLI for RPC methods.

    :param rpc: RPC server to expose as CLI.
    :param exclude_discover: Include `rpc.discover` method in CLI.
    :return: The CLI application.
    """
    openrpc = OpenRPC(**rpc.discover())
    application = Application(name=openrpc.info.title)
    for method in openrpc.methods:
        attributes = {
            "name": method.name,
            "description": method.description,
            "arguments": [
                argument(
                    param.name,
                    optional=_is_optional(param),
                    # Type ignore because schema will never be bool.
                    default=param.schema_.default,  # type: ignore
                    description=_get_type_str(param.schema_),  # type: ignore
                )
                for param in method.params
            ],
            "handle": _get_handler(rpc, method),
        }
        command = type(f"{method.name}Command", (Command,), attributes)
        application.add(command())

    if not exclude_discover:
        # Add discover command manually.
        attributes = {
            "name": "rpc.discover",
            "description": "Get OpenRPC document.",
            "arguments": [],
            "handle": _get_handler(
                rpc,
                Method(
                    name="rpc.discover",
                    params=[],
                    result=ContentDescriptor(
                        name="result", schema=Schema(title="Result", type=None)
                    ),
                ),
            ),
        }
        command = type("rpc.discoverCommand", (Command,), attributes)
        application.add(command())

    return application


def _get_handler(rpc: RPCServer, method: Method) -> Callable:
    async def _handle(self: Command) -> None:
        if method.param_structure is ParamStructure.BY_NAME:
            params = ", ".join(
                f'"{param.name}": {_param_str(arg, param)}'
                for param in method.params
                if (arg := self.argument(param.name)) is not None
            )
            params = "{" + params + "}"
        else:
            params = ", ".join(
                _param_str(arg, param)
                for param in method.params
                if (arg := self.argument(param.name)) is not None
            )
            params = "[" + params + "]"

        req = '{"id": 1, "method": "%s", "params": %s, "jsonrpc": "2.0"}' % (
            method.name,
            params,
        )
        # Response is never None because we don't use notifications.
        response = await rpc.process_request_async(req) or ""
        parsed_response = json.loads(response)
        if "result" in parsed_response:
            self.line(f"<info>{json.dumps(parsed_response['result'])}<info>")
        else:
            self.line(f"<error>{json.dumps(parsed_response['error'])}<error>")

    def _run_handle(self: Command) -> None:
        asyncio.run(_handle(self))

    return _run_handle


def _param_str(value: Any, param: ContentDescriptor) -> str:
    str_val = str(value)
    # Type ignore because schema will never be bool.
    if (
        param.schema_.type != "string"  # type: ignore
        and re.match(r"^\d*\.?\d+$", str_val)
        or str_val.lower() in ["true", "false", "null"]
        or str_val.startswith(("[", "{"))
    ):
        return str_val
    return f'"{str_val}"'


def _is_optional(param: ContentDescriptor) -> bool:
    # Type ignore because schema will never be bool.
    return (
        "default" in param.schema_.model_fields_set  # type: ignore
        or not param.required
    )


# Type ignore because schema will never be bool.
def _get_type_str(schema: Schema) -> str:
    if schema.ref:
        return schema.ref.removeprefix("#/components/schemas/")
    if schema.any_of:
        return " | ".join(_get_type_str(s) for s in schema.any_of)  # type: ignore
    if schema.type == "array" and schema.items:
        array_type = _get_type_str(schema.items)  # type: ignore
        return f"array[{array_type}]"
    return str(schema.type) or "any"
