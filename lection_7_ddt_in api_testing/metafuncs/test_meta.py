# https://docs.pytest.org/en/stable/parametrize.html#parametrize-basics
# Should pass --input as param to pytest


def test_valid_string(input):
    assert input.isalpha(), "Contains not only letters"


def test_upper_string(input):
    assert input.isupper(), "Not upper case string"


def test_compute(limited_param):
    assert limited_param < 4


# def test_param(limited_param):
#     assert not limited_param