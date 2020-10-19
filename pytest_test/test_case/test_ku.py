import yaml, pytest


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./test1.yml")))
    def test_demo1(self, env):
        if "dev" in env:
            print("这是测试环境")
            print(type(env))
