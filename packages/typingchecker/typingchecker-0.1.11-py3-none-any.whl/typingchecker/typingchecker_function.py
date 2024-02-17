from typing import (
    get_type_hints,
    get_origin,
    get_args,
    Union,
    Any,
    Callable,
    Optional,
)
from collections.abc import Callable as Callable_abc
import inspect
from functools import wraps


def check_types(warnings: bool = True, strictfloat: bool = False):
    """
    A decorator that checks the types of the arguments passed to a function.
    It raises a TypeError if the type of an argument is not compatible with the type hint.

    Parameters:
    -----------
    warnings : bool, optional
        Whether to print warnings when a type cannot be checked, by default True
    strictfloat : bool, optional
        If True, ints will raise an error if a float is expected, by default False, in
        which case ints will pass and if possible will be converted to floats
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ### get type hints and variable names
            hints = get_type_hints(func)
            var_names = list(inspect.signature(func).parameters.keys())

            args = list(args)

            ### check args
            for arg_idx, arg in enumerate(args):
                arg_name = var_names[arg_idx]
                if arg_name in hints.keys():
                    check_type_hint(
                        var_name=arg_name,
                        var=args,
                        var_idx=arg_idx,
                        type_hint=hints[arg_name],
                        func=func,
                        warnings=warnings,
                        strictfloat=strictfloat,
                    )

            ### check kwargs
            for kwarg_name, kwarg in kwargs.items():
                if kwarg_name in hints.keys():
                    check_type_hint(
                        var_name=kwarg_name,
                        var=kwargs,
                        var_idx=kwarg_name,
                        type_hint=hints[kwarg_name],
                        func=func,
                        warnings=warnings,
                        strictfloat=strictfloat,
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def check_class_base_rec(var_name, func, type_hint, args, base):
    ### check if args of type hint is equal to base, if yes, return None
    if not args == base:
        ### if not equal go deeper with base
        if base == None:
            ### if base already None, raise TypeError
            raise TypeError(
                f"Parameter {var_name} of function {func} should be a class of {get_args(type_hint)[0]}"
            )
        else:
            ### go deeper and check base of base of base
            return check_class_base_rec(var_name, func, type_hint, args, base.__base__)
    else:
        return None


def check_type_hint(
    var_name: str,
    var: Any,
    var_idx: Any,
    type_hint: type,
    func: Callable,
    warnings: bool,
    strictfloat: bool = False,
    current_var: Optional[Any] = None,
    current_type_hint: Optional[type] = None,
) -> None:
    """
    Check if the type of the variable is compatible with the type hint

    Parameters
    ----------
    var_name : str
        Name of the variable
    var : Any
        List or dict containing variable to check
    var_idx : Any
        Index or key of the variable to check
    type_hint : type
        Type hint of the variable
    func : function
        Function that is checked
    warnings : bool, optional
        Whether to print warnings when a type cannot be checked, by default True
    strictfloat : bool, optional
        If True, ints will raise an error if a float is expected, by default False, in which case ints will be converted to floats
    current_var : Any, optional
        List or dict containing current variable to check, used for recursive calls, by default None
    current_type_hint : type, optional
        Current type hint of the variable, used for recursive calls, by default None
    """

    ### set current_var and current_type_hint to var and type_hint if they are None
    if current_var is None:
        current_var = var
    if current_type_hint is None:
        current_type_hint = type_hint

    # ### debug print
    # if var_name == "n":
    #     print(
    #         f"var_name: {var_name}\nvar: {current_var[var_idx]}\nvar_type: {type(current_var[var_idx])}\ncurrent_type_hint: {current_type_hint}\norigin: {get_origin(current_type_hint)}\nargs: {get_args(current_type_hint)}"
    #     )

    ### depending on origin of type hint doe different things
    ### if origin is type
    ### check if args of type hint is equal to var
    ### if not, check if equal to base of var recursively
    ### if never true, raise TypeError
    if get_origin(current_type_hint) is type:
        ### Type expects a class, first check if var is a class
        if not inspect.isclass(current_var[var_idx]):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be a class of {get_args(type_hint)[0]}"
            )
        ### check if args of type hint is equal to var, if yes, return None
        if get_args(current_type_hint)[0] == current_var[var_idx]:
            return None
        else:
            ### if not equal, check if base class is equal to args of type hint
            return check_class_base_rec(
                var_name,
                func,
                type_hint,
                args=get_args(current_type_hint)[0],
                base=current_var[var_idx].__base__,
            )

    ### if origin is dict
    ### check if type is dict
    ### check if type of all keys and vals are correct
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is dict:
        ### check if type is dict
        if not isinstance(current_var[var_idx], dict):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### passed dict check, now check if type of keys and vals are correct
        type_key = get_args(current_type_hint)[0]
        type_val = get_args(current_type_hint)[1]
        for key, val in current_var[var_idx].items():
            check_type_hint(
                var_name=var_name,
                var=var,
                var_idx=list(current_var[var_idx].keys()).index(key),
                type_hint=type_hint,
                func=func,
                warnings=warnings,
                strictfloat=strictfloat,
                current_var=list(current_var[var_idx].keys()),
                current_type_hint=type_key,
            )
            check_type_hint(
                var_name=var_name,
                var=var,
                var_idx=key,
                type_hint=type_hint,
                func=func,
                warnings=warnings,
                strictfloat=strictfloat,
                current_var=current_var[var_idx],
                current_type_hint=type_val,
            )
        ### variable passed all checks, return None
        return None

    ### if origin is list
    ### check if type is list
    ### check if type of all elements is correct
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is list:
        ### check if type is list
        if not isinstance(current_var[var_idx], list):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### passed list check, now check if type of all elements is correct
        ### if only one type is expected within list --> check all elements against this
        ### type
        if len(get_args(current_type_hint)) == 1:
            type_element = get_args(current_type_hint)[0]
            for element_idx in range(len(current_var[var_idx])):
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    var_idx=element_idx,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    strictfloat=strictfloat,
                    current_var=current_var[var_idx],
                    current_type_hint=type_element,
                )
        ### if multiple types are expected within list --> list should have the same
        ### length as the number of types and the types should be in the same order
        elif len(get_args(current_type_hint)) == len(current_var[var_idx]):
            for element_idx, type_element in enumerate(get_args(current_type_hint)):
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    var_idx=element_idx,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    strictfloat=strictfloat,
                    current_var=current_var[var_idx],
                    current_type_hint=type_element,
                )
        else:
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )

        ### variable passed all checks, return None
        return None

    ### if origin is tuple
    ### check if type is tuple
    ### check if type of all elements is correct
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is tuple:
        ### check if type is tuple
        if not isinstance(current_var[var_idx], tuple):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### passed tuple check, now check if type of all elements is correct
        ### if only one type is expected within tuple --> check all elements against this
        ### type
        if len(get_args(current_type_hint)) == 1:
            type_element = get_args(current_type_hint)[0]
            for element_idx in range(len(current_var[var_idx])):
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    var_idx=element_idx,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    strictfloat=strictfloat,
                    current_var=current_var[var_idx],
                    current_type_hint=type_element,
                )
        ### if multiple types are expected within tuple --> tuple should have the same
        ### length as the number of types and the types should be in the same order
        elif len(get_args(current_type_hint)) == len(current_var[var_idx]):
            for element_idx, type_element in enumerate(get_args(current_type_hint)):
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    var_idx=element_idx,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    strictfloat=strictfloat,
                    current_var=current_var[var_idx],
                    current_type_hint=type_element,
                )
        else:
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )

        ### variable passed all checks, return None
        return None

    ### if origin is Union
    ### check if variable is one of the types in the union
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is Union or get_origin(
        current_type_hint
    ) is type(str | int):
        ### check if variable is any of the types in the union
        for type_ in get_args(current_type_hint):
            ### need a try except here because we want to check all types in the union and not stop at the first one that fails
            try:
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    var_idx=var_idx,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    strictfloat=strictfloat,
                    current_var=current_var,
                    current_type_hint=type_,
                )
                ### variable passed one check, return None
                return None
            except:
                pass
        ### variable did not pass any checks, raise TypeError
        raise TypeError(
            f"Parameter {var_name} of function {func} should be {type_hint}"
        )

    ### if origin is None, its a simple type and we can check it directly using isinstance
    elif get_origin(current_type_hint) is None:
        ### catch Any type hint, which should always pass
        if current_type_hint is Any:
            return None
        ### check if variable is an instance of the type hint, if not raise TypeError
        if not isinstance(current_var[var_idx], current_type_hint):
            ### catch if float type is expected as type hint but the type of the variable is int
            ### this should not raise an error ints can simply be converted to float (nothing is lost, in contrast to float->int)
            if (
                current_type_hint is float
                and isinstance(current_var[var_idx], int)
                and not strictfloat
            ):
                ### try to convert int to float
                try:
                    current_var[var_idx] = float(current_var[var_idx])
                except:
                    pass
                return None
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        else:
            return None

    ### if origin is Callable check if variable is callable
    elif get_origin(current_type_hint) is Callable_abc:
        ### check if variable is callable
        if not callable(current_var[var_idx]):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### if there are args for the Callable type hint print that the arguments of
        ### Callable are not checked
        if get_args(current_type_hint) != ():
            if warnings:
                print(
                    f"WARNING check_type_hint: Arguments of Callable type hint for variable {var_name} of function {func} are not checked."
                )
        ### variable passed all checks, return None
        return None

    ### if variable passed all checks without errors or returning, print that the type cannot be checked
    if warnings:
        print(
            f"WARNING check_type_hint: Variable {var_name} of function {func} could not be checked."
        )
    return None
