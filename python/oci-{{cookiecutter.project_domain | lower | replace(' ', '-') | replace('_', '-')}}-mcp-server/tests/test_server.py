"""
Copyright (c) 2025, Oracle and/or its affiliates.
Licensed under the Universal Permissive License v1.0 as shown at
https://oss.oracle.com/licenses/upl.
"""


"""Tests for the oci-{{cookiecutter.project_domain}} MCP Server."""

import pytest
from oracle.oci-{{cookiecutter.project_domain | lower | replace(' ', '-') | replace('_', '-') | replace('-', '_')}}_mcp_server.server import example_tool

@pytest.mark.asyncio
async def test_example_tool():
    # Arrange
    test_query = "test query"
    expected_project_name = "oracle oci-{{cookiecutter.project_domain}} MCP Server"
    expected_response = f"Hello from {expected_project_name}! Your query was {test_query}. Replace this with your tool's logic"

    # Act
    result = await example_tool(test_query)

    # Assert
    assert result == expected_response

@pytest.mark.asyncio
async def test_example_tool_failure():
    # Arrange
    test_query = "test query"
    expected_project_name = "oracle oci-{{cookiecutter.project_domain}} MCP Server"
    expected_response = f"Hello from {expected_project_name}! Your query was {test_query}. Replace this your tool's new logic"

    # Act
    result = await example_tool(test_query)

    # Assert
    assert result != expected_response
