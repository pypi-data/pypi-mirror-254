from typingchecker import check_types
import pytest


class checked_class:
    @check_types()
    def __init__(
        self,
        a: int,
        b: float,
        c: list[float] = [1.0, 2.0, 3.0],
        d: dict[str, float] = {"a": 1.0, "b": 2.0, "c": 3.0},
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


def test_check_types_convert_int():
    ####################################################################################
    ############################   RAISING NO ERRORS   #################################
    ####################################################################################

    ### give an int to b, this should be converted to float
    checked_obj = checked_class(1, 2)
    assert isinstance(checked_obj.a, int) and isinstance(
        checked_obj.b, float
    ), "check_types did not convert int to float"

    ### give a list of ints to c, this should be converted to list of floats
    checked_obj = checked_class(1, 2.0, [1, 6.0, 3])
    assert (
        isinstance(checked_obj.a, int)
        and isinstance(checked_obj.b, float)
        and isinstance(checked_obj.c[0], float)
    ), "check_types did not convert list of int to list of float"

    ### give a dict with ints to d, this should be converted to dict with floats
    checked_obj = checked_class(1, 2.0, [1, 6.0, 3], {"a": 1, "b": 2.0, "c": 3})
    assert (
        isinstance(checked_obj.a, int)
        and isinstance(checked_obj.b, float)
        and isinstance(checked_obj.c[0], float)
        and isinstance(checked_obj.d["a"], float)
    ), "check_types did not convert list of int to list of float"

    ####################################################################################
    ##############################   RAISING ERRORS   ##################################
    ####################################################################################

    ### keys should still be strings
    with pytest.raises(TypeError):
        checked_obj = checked_class(1, 2.0, [1, 6.0, 3], {1: 1, "b": 2.0, "c": 3})

    ### floats instead of ints should still raise an error
    with pytest.raises(TypeError):
        checked_obj = checked_class(1.5, 2.0, [1, 6.0, 3], {"a": 1, "b": 2.0, "c": 3})


if __name__ == "__main__":
    test_check_types_convert_int()
