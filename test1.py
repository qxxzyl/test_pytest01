import pytest

def test_a():
    print("\n111")
    assert 1

def test_b():
    print("\n2222")
    assert 0

# -s 代表输出打印日志
if __name__ == '__main__':
    pytest.main("-s test1.py")

# .代表成功 F代表失败

