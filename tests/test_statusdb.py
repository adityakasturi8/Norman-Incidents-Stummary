import pytest
from project0 import project0

def test_statusdb():
    db = project0.createdb()
    store_data = project0.status(db)
    assert store_data is not None
