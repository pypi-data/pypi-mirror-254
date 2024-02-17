from typingchecker import check_types
import pytest


@check_types()
def tmp_test(dict_inside: dict[str, float], var_inside: float = 1.0):
    assert (
        isinstance(dict_inside["a"], float)
        and isinstance(dict_inside["b"], float)
        and isinstance(var_inside, float)
    ), "with float type hints, the types within the function should be converted to float"


@check_types(strictfloat=True)
def tmp_test_strict(dict_inside: dict[str, float], var_inside: float = 1.0):
    assert (
        isinstance(dict_inside["a"], float)
        and isinstance(dict_inside["b"], float)
        and isinstance(var_inside, float)
    ), "with float type hints, the types within the function should be converted to float"


def test_check_types_strictfloat():
    ####################################################################################
    ############################   RAISING NO ERRORS   #################################
    ####################################################################################

    ### does not raise an error
    ### because by default int values are converted to float if the type hint is float
    ### but the convertion to float does also affect the value outside of the function! (in case of dicts and lists)
    ### so if you have a list or dict containing int values and you do not want to unintentional convert them to float you can use strictfloat=True
    dict_outside = {"a": 1, "b": 2}
    tmp_test(dict_outside)
    assert isinstance(dict_outside["a"], float) and isinstance(
        dict_outside["b"], float
    ), "by default int values should be converted to float, this should also affect the value outside of the function!"

    ### for simple variables like b, the value outside of the function is not affected, but inside the function it's converted to float
    dict_outside = {"a": 1, "b": 2}
    var_outside = 2
    tmp_test(dict_outside, var_outside)
    assert isinstance(
        var_outside, int
    ), "the value outside of the function should not be affected by the convertion to float"

    ####################################################################################
    ##############################   RAISING ERRORS   ##################################
    ####################################################################################

    ### should raise an error because stricfloat=True and the values of "a" and "b" are an int instead of float
    dict_outside = {"a": 1, "b": 2}
    with pytest.raises(TypeError):
        tmp_test_strict(dict_outside)

    ### should also raise an error because stricfloat=True and here b is an int instead of float
    dict_outside = {"a": 1.0, "b": 2.0}
    with pytest.raises(TypeError):
        tmp_test_strict(dict_outside, 2)


if __name__ == "__main__":
    test_check_types_strictfloat()
