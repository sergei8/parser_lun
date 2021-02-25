import pytest
from extract_numbers import \
    get_total_price, \
    get_romms, \
    get_price_sqm, \
    _get_level_property, \
    get_level, \
    get_year, \
    _get_area_property
    

    
@pytest.fixture
def lun_data():
    return \
"""
115 000 $,2 комнаты,1575 $ за м²,21 из 25,год постройки 2015,кирпичные,73 / 37 / 15 м²,ул.  Малиновского, 4в
"""

def test_get_total_price(lun_data):
    expected = [115000.0, None]
    actual = get_total_price(lun_data)
    assert actual in expected
    
def test_get_rooms(lun_data):
    expected = [2, None]
    actual = get_romms(lun_data)
    actual = get_romms(lun_data)
    assert actual == expected[0]
    assert actual in expected
    
def test_get_price_sqm(lun_data):
    expected = [1575, None]
    actual = get_price_sqm(lun_data)
    assert actual == expected[0]
    
def test_get_level_property(lun_data):
    expected = [(21, 25), None]
    actual = _get_level_property(lun_data, 3)
    assert actual in expected
    
def test_get_level(lun_data):
    expected = [21, None]
    actual = get_level(lun_data)
    assert actual in expected
    
def test_get_year(lun_data):
    expected = [2015, None]
    actual = get_year(lun_data)
    assert actual == 2015
    assert actual in expected
    
def test_get_area_property(lun_data):
    expected = [(73.0, 37.0, 15.0), None]
    actual = _get_area_property(lun_data, 6)
    assert actual in expected
    
    
    