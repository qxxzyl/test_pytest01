import pytest


class TestA:

    def test_a(self):
        print("\n1111")

    @pytest.mark.skipif
    def test_b(self):
        print("\n22222")
        assert 0

    @pytest.mark.xfail  #虽然标记失败 但是函数还是会运行一次 要确定一下是否真的失败
    def test_c(self):
        print("\n3333")
        assert 0

    # @pytest.mark.parametrize("a,b", [(1, 2), (0, 3)])
    @pytest.mark.parametrize("a", [3, 6])
    def test_d(self,a):
        print("a====%d"%a)
        # print("b====%d"%b)


# 较小的整数>较大的整数 > 无标记
# 0>较小的整数
# 较小的负数 > 较大的负数
# 无标记 >较小负数>较大的负数
# 结论 0 > 较小的整数>较大的整数 >无标记 > 较小的负数>较大的负数




