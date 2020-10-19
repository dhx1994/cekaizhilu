import pytest, yaml, selenium
import pytest_ordering


def setup_module():
    print("仅在模块开始时调用")


def teardown_module():
    print("仅在模块结束时调用")


class TestLogin():
    @pytest.fixture()
    def login(self):
        print("需要调用登录方法")
        return True

    # @classmethod
    # def setup_class(cls):
    #     print("在类开始时调用")
    # @classmethod
    # def teardown_class(cls):
    #     print("仅在类结束时调用")
    # def setup(self):
    #     print("仅在方法开始前调用")
    # def teardown(self):
    #     print("仅在方法结束时调用")
    @pytest.mark.run(order=2)
    def test_login(self):
        assert 1 == 1
        print("这个是第一个测试用例")

    @pytest.mark.run(order=0)
    def test_one(self, login):
        print(login)
        x = "this"
        assert "s" in x
        print("this is second testcase")

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("这个是第二个测试用例")
