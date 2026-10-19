"""Unit tests for the JSONPlaceholder API client."""

from unittest.mock import Mock, patch

import pytest
import requests

from api_client import get_user


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_returns_user_and_sends_request():
    expected_user = {
        "id": 1,
        "name": "Test User",
        "email": "test@example.com",
    }

    with patch("api_client.requests.get") as mock_get:
        response = Mock()
        response.status_code = 200
        response.json.return_value = expected_user
        mock_get.return_value = response

        user = get_user(1)

    assert user == expected_user
    mock_get.assert_called_once_with(
        f"{BASE_URL}/users/1",
        timeout=10,
    )
    response.raise_for_status.assert_called_once_with()
    response.json.assert_called_once_with()


@pytest.mark.parametrize("status_code", [400, 404, 500])
def test_get_user_raises_http_error(status_code):
    with patch("api_client.requests.get") as mock_get:
        response = Mock()
        response.status_code = status_code

        def raise_for_status():
            if response.status_code >= 400:
                raise requests.HTTPError(
                    f"HTTP {response.status_code} error"
                )

        response.raise_for_status.side_effect = raise_for_status
        mock_get.return_value = response

        with pytest.raises(requests.HTTPError):
            get_user(1)

    response.raise_for_status.assert_called_once_with()
    mock_get.assert_called_once_with(
        f"{BASE_URL}/users/1",
        timeout=10,
    )


def test_get_user_propagates_timeout():
    with patch("api_client.requests.get") as mock_get:
        mock_get.side_effect = requests.Timeout("Request timed out")

        with pytest.raises(requests.Timeout):
            get_user(1)

    mock_get.assert_called_once_with(
        f"{BASE_URL}/users/1",
        timeout=10,
    )
