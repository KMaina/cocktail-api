import pytest

pytest_plugins = (
    "cocktails.tests.fixtures.drinks",
)

@pytest.fixture(scope="function")
def client():
    from rest_framework.test import APIClient
    return APIClient()