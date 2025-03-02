import pytest


def test_first_code():
    print("This is my first test")

# @pytest.mark.xfail
@pytest.mark.skip(reason:This test is no longer in use)
def test_sample_code():
    assert 2 == 3
    print("This is sample code")