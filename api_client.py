"""Small client for the JSONPlaceholder users endpoint."""

from typing import Any

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
REQUEST_TIMEOUT = 10


def get_user(user_id: int) -> dict[str, Any]:
    """Fetch a user by ID and return the decoded JSON response.

    Raises:
        requests.exceptions.HTTPError: If the server returns an HTTP error.
        requests.exceptions.RequestException: If the request fails.
    """
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
