from pytest import mark

class TestDummy():
    @mark.smoke
    @mark.model
    def test_dummy(self):
        assert True

    @mark.API
    def test_dummy_2(self):
        assert True