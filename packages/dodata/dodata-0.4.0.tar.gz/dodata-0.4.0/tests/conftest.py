import pytest
import doplaydo.dodata as dd
from sqlmodel import Session


@pytest.fixture
def session() -> Session:
    return dd.session
