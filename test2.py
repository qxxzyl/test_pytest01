class TestA:
    # def setup(self):
    #     print("aaa")
    #
    # def teardown(self):
    #     print("bbb")

    def setup_class(self):
        print("aaa")

    def teardown_class(self):
        print("bbb")

    def test_a(self):
        print("111")

    def test_b(self):
        print("222")



