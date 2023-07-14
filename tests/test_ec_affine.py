import pytest
from zkmarek.ec_affine import ECAffine
from zkmarek.field import Field


class TestECAffine:
    def test_init(self):
        actual = ECAffine([Field(1, 41), Field(7, 41)])
        assert actual.coords == [Field(1, 41), Field(7, 41)]

    def test_init_wrong_dimension(self):
        with pytest.raises(AssertionError):
            ECAffine([Field(1, 41)])
        with pytest.raises(AssertionError):
            ECAffine([Field(1, 7), Field(2, 7), Field(2, 7)])

    def test_init_various_orders(self):
        with pytest.raises(AssertionError):
            ECAffine([Field(1, 17), Field(2, 41)])

    def test_from_int(self):
        actual = ECAffine.from_int([1, 7], 41)
        assert actual.coords == [Field(1, 41), Field(7, 41)]

