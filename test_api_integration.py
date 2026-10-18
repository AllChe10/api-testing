import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.integration
def test_get_user_from_live_api():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "name" in user


@pytest.mark.integration
def test_unknown_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/unknown-endpoint", timeout=10)

    assert response.status_code == 404


@pytest.mark.integration
def test_live_user_has_expected_fields():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)

    assert response.status_code == 200
    user = response.json()

    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)
    assert user["email"] != ""
