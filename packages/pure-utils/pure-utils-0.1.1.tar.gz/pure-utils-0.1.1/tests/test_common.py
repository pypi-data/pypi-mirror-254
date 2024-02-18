import pytest
from common import Singleton


def test_singletone_class():
    class SigletonClass(metaclass=Singleton):
        pass

    class RegularClass:
        pass

    a = SigletonClass()
    b = SigletonClass()
    c = RegularClass()

    assert isinstance(SigletonClass, Singleton)
    assert isinstance(a, SigletonClass)
    assert isinstance(b, SigletonClass)
    assert isinstance(c, RegularClass)
    assert a == b
    assert c != a and c != b
