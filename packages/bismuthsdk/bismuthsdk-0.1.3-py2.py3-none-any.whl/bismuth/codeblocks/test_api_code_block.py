import pytest
from flask import Flask
from unittest.mock import MagicMock
from .api_code_block import (
    APICodeBlock,
)


# Fixture to setup the APICodeBlock with mocked routes
@pytest.fixture
def api_block():
    api_block = APICodeBlock(
        app_config={
            "TESTING": True,
        }
    )
    return api_block


def test_add_route(api_block):
    mock_func = MagicMock(return_value={"message": "mock response"})

    with api_block.app.test_client() as client:
        api_block.add_route("/mock", "GET", {"GET": mock_func})
        response = client.get("/mock")
        assert response.status_code == 200
        assert response.json == {"message": "mock response"}
        mock_func.assert_called_once()
