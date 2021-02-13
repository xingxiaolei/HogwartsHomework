import pytest
import yaml
import allure

with open('./data1.yaml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_id = datas['add']['myid']

    div_data = datas['div']['datas']
    div_id = datas['div']['myid']

    sub_data = datas['sub']['datas']
    sub_id = datas['sub']['myid']

    mul_data = datas['mul']['datas']
    mul_id = datas['mul']['myid']


@pytest.fixture(params=add_data, ids=add_id)
def get_add_datas(request):
    datas = request.param
    return datas


@pytest.fixture(params=div_data, ids=div_id)
def get_div_datas(request):
    datas = request.param
    yield datas

@pytest.fixture()
def fixture_demo():
    print('开始计算')
    yield
    print('结束计算')


@allure.feature('测试计算器')
class TestClac:
    '''
    加法和除法使用conftest并且参数化；
    减法和乘法使用本文件的fixture和parametrize参数化
    '''

    @allure.story('测试加法运算')
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_datas):
        '''测试加法运算'''
        actual = get_calc.add(get_add_datas[0], get_add_datas[1])
        if isinstance(actual, float):
            actual = round(actual, 2)
        assert actual == get_add_datas[2]

    @allure.story('测试除法运算')
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_datas):
        '''测试除法运算'''
        if get_div_datas[1] == 0:
            print('分母不能为零')
            assert False
        else:
            actual = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(actual, float):
                actual = round(actual, 2)
            assert actual == get_div_datas[2]

    @allure.story('测试减法运算')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expect", sub_data, ids=sub_id)
    def test_sub(self, fixture_demo, get_calc, a, b, expect):
        actual = get_calc.sub(a, b)
        if isinstance(actual, float):
            actual = round(actual, 2)
        assert actual == expect

    @allure.story('测试乘法运算')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expect", mul_data, ids=mul_id)
    def test_mul(self, fixture_demo, get_calc, a, b, expect):
        actual = get_calc.mul(a, b)
        if isinstance(actual, float):
            actual = round(actual, 2)
        assert actual == expect