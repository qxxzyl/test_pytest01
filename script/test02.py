class TestB:

    def test_a(self):
        print("\nscript111")
        assert 1

    def test_b(self):
       print("\nscript2222")
       assert 0

    #当是类级别
    def setup_class(self):
        print("setupclass")

    def teardown_class(self):
        print("teardown")