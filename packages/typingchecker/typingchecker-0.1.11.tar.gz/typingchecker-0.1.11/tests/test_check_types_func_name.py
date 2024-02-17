from typingchecker import check_types
import pytest


@check_types()
def checked_func_with_name(a: int):
    return a


def test_check_types_func_name():
    ### checked_func_with_name.__name__ should be checked_func_with_name
    assert checked_func_with_name.__name__ == "checked_func_with_name"

    ### giving int should not raise error
    checked_func_with_name(1)

    ### giving float should raise type error
    with pytest.raises(TypeError):
        checked_func_with_name(1.0)
