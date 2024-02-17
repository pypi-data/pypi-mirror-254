from typingchecker import check_types
from typing import Union, Type, Any, Callable
import pytest


class needed_class:
    def __init__(self) -> None:
        pass


### subclass of object, actually the same as needed_class, but for testing...
class needed_obj_class(object):
    def __init__(self) -> None:
        pass


### subclass of int
class needed_int_class(int):
    def __init__(self) -> None:
        pass


class checked_class:
    @check_types()
    def __init__(
        self,
        a: int,
        b: list[list[int]],
        c: Union[needed_class, list[needed_class]],
        d: float | list[float],
        e: dict[str, int],
        # f: Type expects a subclass of the specified class, not an instance
        f: Type[needed_class] = needed_class,
        g: Type[needed_obj_class] = needed_obj_class,
        h: Type[needed_int_class] = needed_int_class,
        # i: this expects a subclass of the object class which should be any class
        i: Type[object] = object,
        j: Type[needed_int_class] | Type[needed_obj_class] = needed_int_class,
        k: tuple[int, str] = (1, "a"),
        l: list[int, str] = [1, "a"],
        m: Any = 5.0,
        n: Callable = lambda x, y: x + y,
    ):
        pass


needed_obj = needed_class()


def test_check_types_decorator():
    ####################################################################################
    ############################   RAISING NO ERRORS   #################################
    ####################################################################################

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
    )

    ### if check_types works, this should not raise an error
    ### d expects float, but int can simply be used as float...
    checked_class(
        1,
        [[1, 2]],
        needed_obj,
        1,
        {"a": 1},
    )

    ### if check_types works, this should not raise an error
    ### d expects float, but int can simply be used as float...
    checked_class(
        1,
        [[1]],
        needed_obj,
        [1],
        {"a": 1},
    )
    ### if check_types works, this should not raise an error
    ### d expects float, but int can simply be used as float...
    checked_class(
        1,
        [[1]],
        needed_obj,
        [1, 2],
        {"a": 1},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1], [2]],
        [needed_obj, needed_obj],
        [1.0, 2.0],
        {"a": 1, "b": 2},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [],
        needed_obj,
        1.0,
        {},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[]],
        [needed_obj],
        [1.0],
        {"a": 1},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        f=needed_class,
        g=needed_obj_class,
        h=needed_int_class,
        i=object,
        j=needed_int_class,
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        f=needed_class,
        g=needed_obj_class,
        h=needed_int_class,
        i=object,
        j=needed_obj_class,
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        f=needed_class,
        g=needed_obj_class,
        h=needed_int_class,
        i=needed_obj_class,
        j=needed_obj_class,
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        f=needed_class,
        g=needed_obj_class,
        h=needed_int_class,
        i=needed_int_class,
        j=needed_obj_class,
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        f=needed_class,
        g=needed_obj_class,
        h=needed_int_class,
        i=needed_class,
        j=needed_obj_class,
    )

    ### if check_types works, this should not raise an error because k is a tuple of int
    ### and str
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        k=(1, "a"),
    )

    ### if check_types works, this should not raise an error because l is a list of int
    ### and str
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        l=[1, "a"],
    )

    ### if check_types works, this should not raise an error because m is of type Any
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        m=5.0,
    )
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        m="5.0",
    )

    ### if check_types works, this should not raise an error because n is of type Callable
    def add(x: int | float, y: str, z: Any) -> float:
        return float(x + y)

    class add_class:
        def __init__(self) -> None:
            pass

        def __call__(self, x: str, y: int, z: Any) -> float:
            return x + y

    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        n=lambda x, y: x + y,
    )
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        n=add,
    )
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
        n=add_class(),
    )

    ####################################################################################
    #############################   RAISING ERRORS   ###################################
    ####################################################################################

    ### if check_types works, this should raise an TypeError because a is not an int
    with pytest.raises(TypeError):
        checked_class(
            "1",
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because a is not an int
    with pytest.raises(TypeError):
        checked_class(
            1.2,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because b is not a list of lists of ints
    with pytest.raises(TypeError):
        checked_class(
            1,
            [1],
            needed_obj,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because c is not a needed_class or a list of needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            "needed_obj",
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because d is not a float or a list of floats
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            "1.0",
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because e is not a dict of str to int
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": "1"},
        )

    ### if check_types works, this should raise an TypeError because c is not an instance of needed_class but the class itself
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_class,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because f is not the expected needed_class but a instance of needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            f=needed_obj,
        )

    ### if check_types works, this should raise an TypeError because h is not the expected needed_int_class but an int instance
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            h=2,
        )

    ### if check_types works, this should raise an TypeError because f expects a specific class and object is too general
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            f=object,
        )

    ### if check_types works, this should raise an TypeError because g expects a specific class and object is too general
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            g=object,
        )

    ### if check_types works, this should raise an TypeError because h expects a specific class and object is too general
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            h=object,
        )

    ### if check_types works, this should raise an TypeError because j expects a specific class and object is too general
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            j=object,
        )

    ### if check_types works, this should raise an TypeError because j expects a different class than needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            j=needed_class,
        )

    ### if check_types works, this should raise an TypeError because j expects a class not an int
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            j=1,
        )

    ### if check_types works, this should raise an TypeError because g expects a different class than needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            g=needed_class,
        )

    ### if check_types works, this should raise an TypeError because h expects a different class than needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            h=needed_class,
        )

    ### if check_types works, this should raise an TypeError because k expects a tuple like (int, str)
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            k=(1, 2),
        )

    ### if check_types works, this should raise an TypeError because k expects a tuple like (int, str)
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            k=[1, "a"],
        )

    ### if check_types works, this should raise an TypeError because k expects a tuple like (int, str)
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            k=(1, "a", 2),
        )

    ### if check_types works, this should raise an TypeError because l expects a list like [int, str]
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            l=[1, 2],
        )

    ### if check_types works, this should raise an TypeError because l expects a list like [int, str]
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            l=[1, "a", 2],
        )

    ### if check_types works, this should raise an TypeError because l expects a list like [int, str]
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            l=(1, "a"),
        )

    ### if check_types works, this should raise an TypeError because n expects a callable
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
            n=5,
        )


if __name__ == "__main__":
    test_check_types_decorator()
