import pytest
from page.home_page import HomePage


@pytest.fixture(scope="function")
def home_ini():
    yield HomePage()
