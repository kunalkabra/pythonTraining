import pytest


# @pytest.mark.parametrize('x, y, z', [(5, 10, 50), (10, 20, 199), (10, 20, 200)])
# def test_method(x, y, z):
#     assert x*y == z


@pytest.fixture
def input_value():
   input = 39
   return input


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0


def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
