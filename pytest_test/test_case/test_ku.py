import yaml, pytest


def files():
    with open("./test1.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas['add']['dir']
        return add_datas


#  @pytest.mark.parametrize("env,a,b", yaml.safe_load(open("./test1.yml")))
def test_demo1():
    a = files()

    print(type(a))
