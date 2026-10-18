from unittest.mock import Mock, patch

import pytest
import requests

from api_client import get_user


def test_get_user_from_client():
    with patch("api_client.requests.get") as mock_get:
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
        }
        mock_get.return_value = response

        user = get_user(1)

        assert user["id"] == 1
        assert user["name"] == "Test User"
        assert user["email"] == "test@example.com"
        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=10,
        )
        response.raise_for_status.assert_called_once_with()


def test_get_user_raises_error_on_404():
    with patch("api_client.requests.get") as mock_get:
        response = Mock()
        response.status_code = 404
        response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = response

        with pytest.raises(requests.HTTPError):
            get_user(999)


def test_get_user_raises_error_on_server_error():
    with patch("api_client.requests.get") as mock_get:
        response = Mock()
        response.status_code = 500
        response.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
        mock_get.return_value = response

        with pytest.raises(requests.HTTPError):
            get_user(1)


def test_get_user_handles_timeout():
    with patch("api_client.requests.get") as mock_get:
        mock_get.side_effect = requests.Timeout("Request timed out")

        with pytest.raises(requests.Timeout):
            get_user(1)
