import pytest
from extract_numbers import \
    get_total_price
    
@pytest.fixture
def lun_data():
    return \
"""
115 000 $,2 комнаты,1575 $ за м²,21 из 25,год постройки2015,кирпичные,73 / 37 / 15 м²,ул.  Малиновского, 4в
"""

def test_get_total_price(lun_data):
    expected = [115000, None]
    actual = get_total_price(lun_data)
    assert actual in expected