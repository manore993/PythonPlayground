import utils
import pytest
from utils import my_sum, reverse_str, main_function, create_player, perimeter

def test_sum_of_two_positives_numbers():
    assert my_sum(1,2) == 3
    assert my_sum(2,1) == 3
    assert my_sum(2,2) == 4

def test_sum_of_neg_and_pos_numbers():
    assert my_sum(-1,2) == 1
    assert my_sum(-2,1) == -1
    assert my_sum(2,-2) ==  0

def test_sum_fail_for_string():
    with pytest.raises(Exception):
        my_sum("a", 3)
    with pytest.raises(Exception):
        my_sum(1, "z")
            
def test_should_reverse_string():
    assert reverse_str('abc') == 'cba'

def test_main_function(monkeypatch):

    def mockreturn():
        return 100
    
    monkeypatch.setattr(utils, 'request', mockreturn)

    expected_value = 100 
    assert main_function() == expected_value

def test_main_function_pytest_plugin_mock(mocker):
    mocker.patch('utils.request', return_value=100)
    expected_value = 100
    assert main_function() == expected_value

class MockResponse:

    @staticmethod
    def get_info():
        return {"name": "test", "level" : 200}

def test_create_player(monkeypatch):
    
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("utils.Player", mock_get)
    
    expected_value = {"name": "test", "level" : 200}
    assert create_player() == expected_value

def test_perimeter(mocker):
    mocker.patch.object(utils, 'PI', 3.14)
    expected_value = 12.56
    assert perimeter(2) == expected_value