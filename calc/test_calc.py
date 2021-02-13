import pytest
import yaml
from calc.calc_func import Calculator

with open('./data.yaml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_id = datas['add']['myid']

    div_data = datas['div']['datas']
    div_id = datas['div']['myid']


class TestClac:
    def setup_class(self):
        print('开始计算')
        self.calc = Calculator()

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize("a, b, expect", add_data, ids=add_id)
    def test_add(self, a, b, expect):
        '''测试加法运算'''
        actual = self.calc.add(a,b)
        if isinstance(actual, float):
            actual = round(actual,2)
        assert actual == expect

    @pytest.mark.parametrize("a, b, expect", div_data, ids=div_id)
    def test_div(self, a, b, expect):
        '''测试除法运算'''
        if b == 0:
            print('分母不能为零')
            assert False
        else:
            actual = self.calc.div(a, b)
            if isinstance(actual, float):
                actual = round(actual, 2)
            assert actual == expect