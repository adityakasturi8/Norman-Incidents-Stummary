import sys
sys.path.append('..')

import pytest
from project0 import project0

def test_extract_incidents():
    url = r"https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf"

    incident_data = project0.fetch_incidents(url)
    store_data = project0.extract_incidents(incident_data)
    assert store_data is not None
