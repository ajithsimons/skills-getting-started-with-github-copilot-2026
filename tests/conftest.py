import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module
from src.app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: snapshot the in-memory activities dict before each test
    original = copy.deepcopy(app_module.activities)
    yield
    # Restore after test to prevent cross-test pollution
    app_module.activities.clear()
    app_module.activities.update(original)
