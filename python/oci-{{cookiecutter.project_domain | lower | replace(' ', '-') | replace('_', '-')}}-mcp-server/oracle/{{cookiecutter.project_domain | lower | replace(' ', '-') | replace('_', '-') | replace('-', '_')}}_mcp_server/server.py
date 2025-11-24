"""
Copyright (c) 2025, Oracle and/or its affiliates.
Licensed under the Universal Permissive License v1.0 as shown at
https://oss.oracle.com/licenses/upl.
"""

"""oracle oci-{{cookiecutter.project_domain}} MCP Server implementation."""

from loguru import logger
from mcp.server.fastmcp import FastMCP
from typing import Literal


mcp = FastMCP(
    "oracle.oci-{{cookiecutter.project_domain | lower | replace(' ', '-') | replace('_', '-')}}-mcp-server",
    instructions='{{cookiecutter.instructions | replace('\'', '\'\'')}}',
    dependencies=[
        'pydantic',
        'loguru',
    ],
)


@mcp.tool(name='ExampleTool')
async def example_tool(
    query: str,
) -> str:
    """Example tool implementation.

    Replace this with your own tool implementation.
    """
    project_name = 'oracle {{cookiecutter.project_domain}} MCP Server'
    return (
        f"Hello from {project_name}! Your query was {query}. Replace this with your tool's logic"
    )

def main():
    """Run the MCP server with CLI argument support."""
    mcp.run()


if __name__ == '__main__':
    main()
