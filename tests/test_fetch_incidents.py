import sys
sys.path.append('..')

from project0 import project0


import pytest 

def test_fetch_incidents():
    url = r"https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"
    store_data = project0.fetch_incidents(url)
    assert store_data is not None
    

