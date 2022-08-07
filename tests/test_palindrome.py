import pytest
from utilities.palindrome import is_palindrome


@pytest.mark.parametrize("test_input, expected", [
    ('Race Car', True),
    ('eye', True),
    ('_eye', True),
    ('A man, a plan, a canal. Panama', True),
    ('never odd or even', True),
    ('0_0 (: /-\\ :), 0-0', True),
    ('1 eye for of 1 eye.', False)
])
def test_palindrome(test_input, expected):
    assert is_palindrome(test_input) is expected
