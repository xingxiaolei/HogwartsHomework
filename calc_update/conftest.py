import pytest
from calc.calc_func import Calculator


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    print('开始计算啦')
    yield calc
    print('结束计算啦')
