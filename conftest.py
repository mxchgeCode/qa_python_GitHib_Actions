import pytest
from main import BooksCollector

@pytest.fixture
def collect():
    collect = BooksCollector()
    return collect