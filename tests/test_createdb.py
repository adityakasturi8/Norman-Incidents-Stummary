import sys
sys.path.append('..')
import pytest
from project0 import project0

def test_createdb():
     db = 'example.db'
     store_data = project0.createdb(db)
     assert store_data is not None

