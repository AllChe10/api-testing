"""Integration tests that make real requests to JSONPlaceholder."""

import pytest

from api_client import get_user


@pytest.mark.integration
def test_get_user_from_live_api():
    user = get_user(1)

    assert user["id"] == 1
    assert isinstance(user["name"], str)
    assert user["name"]
    assert isinstance(user["email"], str)
    assert user["email"]
