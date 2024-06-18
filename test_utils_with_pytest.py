import utils
import pytest
from utils import my_sum, reverse_str, main_function;

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