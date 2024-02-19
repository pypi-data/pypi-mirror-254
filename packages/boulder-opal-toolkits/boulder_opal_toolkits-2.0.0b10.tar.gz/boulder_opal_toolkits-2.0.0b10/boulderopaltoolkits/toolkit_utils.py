# Copyright 2024 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Utility functions for exposing and binding toolkits.
"""
from __future__ import annotations

import inspect
from enum import Enum
from functools import (
    partial,
    wraps,
)
from typing import (
    Any,
    Callable,
    Optional,
)

import forge
import numpy as np
from numpydoc.docscrape import NumpyDocString
from qctrlcommons.exceptions import QctrlException
from qctrlcommons.node.wrapper import NodeData
from qctrlcommons.preconditions import check_argument

from boulderopaltoolkits.namespace import Namespace

# parameters like qctrl/graph in the toolkit functions are just placeholder for the actual object
# need to remove them from the doc/signature before binding in python
_EXCLUDE_PARAMETERS = {"qctrl", "graph"}

TOOLKIT_ATTR = "_toolkit_attr"


def expose(*namespaces: Namespace) -> Any:
    """
    Define a decorator that inserts a label of the namespaces for later binding to the
    wrapped object.

    The decorator sets a new attribute defined by TOOLKIT_ATTR to the object, which is a tuple
    of strings defining the namespaces. You can apply this decorator to the toolkit function/class,
    and they will be bound to the corresponding namespaces when initializing the Qctrl/Graph object.
    It also sets a new attribute to the object to allow tracking through the python package.

    For example, to expose a function to one namespace ::

        @expose(Namespace.SUPERCONDUCTING)
        def some_func()

    To expose a function to multiple namespaces, as it maybe be reused for
    different physical systems ::

        @expose(Namespace.SUPERCONDUCTING, Namespace.IONS)
        def some_general_func()
    """
    return partial(_expose, attr=namespaces)


def _expose(obj, attr):
    setattr(obj, TOOLKIT_ATTR, attr)
    namespaces = "_".join([f"{i.name.lower()}" for i in attr])
    method_origin = f"boulder-opal-toolkits.{namespaces}.{getattr(obj, '__name__')}"
    setattr(obj, "method_origin", method_origin)
    return obj


def forge_toolkit(toolkit: Any, obj: Any) -> Any:
    """
    Forge the toolkit object (must be a function or class) for binding.

    Note that when toolkit is a class, we just return it, since it should
    not accept the to-be-bound object, to avoid the cyclic access.

    Parameters
    ----------
    toolkit : Any
        A toolkit function or class to be forged.
    obj : Any
        The object to which the forged toolkit is bound.

    Returns
    -------
    Any
        A forged class/function.

    Raises
    ------
    QctrlException
        If toolkit has an unsupported type.
    """

    if inspect.isfunction(toolkit):
        return _forge_func(toolkit, obj)
    if inspect.isclass(toolkit):
        return toolkit
    raise QctrlException(
        f"Toolkit must either be a function or a class, but got {type(toolkit)}."
    )


def _forge_func(func: Callable, obj: Any) -> Callable:
    """
    Forge toolkit function.
    """

    def forged(*arg, **kwargs):
        if hasattr(obj, "method_origin"):
            obj.method_origin = getattr(func, "method_origin", None)
            result = func(obj, *arg, **kwargs)
            obj.method_origin = None
        else:
            result = func(obj, *arg, **kwargs)

        return result

    _args, _kwargs, _return_type, bind_obj = _get_args_kwargs_return_type(func)

    if not bind_obj:
        return func

    assert func.__doc__ is not None, f"{func} has no doc."
    forged.__doc__ = _clean_doc(func.__doc__)
    forged.__name__ = func.__name__
    sig = forge.sign(*_args, **_kwargs)
    forged = sig(forged)
    forged = forge.returns(_return_type)(forged)

    return forged


def _get_args_kwargs_return_type(func):
    """
    Get the information about the function signature.

    Returns a tuple, where the first element is list of args,
    the second one is a dictionary for kwargs,
    the third one is the type of the returned value,
    and the last one is a boolean to exclude parameters.
    This will be used to forge a new function for binding.
    """
    _args = []
    _kwargs = {}
    bind_obj = False
    _func_inspected = inspect.signature(func)
    for arg_name, _arg in _func_inspected.parameters.items():
        # note that some convenience function might not be fetchable
        if arg_name == "name":
            _kwargs = {"name": forge.kwarg("name", type=Optional[str], default=None)}
        elif arg_name in _EXCLUDE_PARAMETERS:
            bind_obj = True
        else:
            _args.append(
                forge.arg(
                    arg_name, type=_arg.annotation, default=_get_default_arg_val(_arg)
                )
            )

    return _args, _kwargs, _func_inspected.return_annotation, bind_obj


def _get_default_arg_val(arg: inspect.Parameter) -> Any:
    """
    Post process the default value for a given argument:
        - If the default value is an Enum, use the value of the Enum.
        - Otherwise, do nothing.
    """
    default_val = arg.default
    if isinstance(default_val, Enum):
        return default_val.value
    return default_val


def _clean_doc(doc: str) -> str:
    """
    Removes unnecessary part from the doc.
    """
    doc_obj = NumpyDocString(doc)

    doc_obj["Parameters"] = [
        item for item in doc_obj["Parameters"] if item.name not in _EXCLUDE_PARAMETERS
    ]

    return str(doc_obj)


def no_graph_parameters(alternatives: Optional[str]) -> Callable:
    """
    Check that none of the parameters passed to the function are graph objects.

    Use this as a decorator for non-graph functions, to make sure that no
    graph object types are being passed as parameters by accident.

    Parameters
    ----------
    alternatives : str or None
        Text listing alternative functions that do accept graphs and that the
        user might be intending to use instead. If it's None, nothing is
        suggested to the user.

    Returns
    -------
    Callable
        A decorator that adds checks to the beginning of the function to see
        if none of the inputs are graph types, and raises an exception that
        suggests the `alternatives`.

    Examples
    --------
    Create a addition function that only accepts non-Graph objects as input,
    and that suggests `graph.add` as an alternative.

    >>> @no_graph_parameters(alternatives="`graph.add`")
    ... def numpy_add(x, y):
    ...     return x + y
    >>> numpy_add(1, graph.tensor(2))
    qctrlcommons.exceptions.QctrlArgumentsValueError: The parameters of
    `numpy_add` cannot be graph objects. Perhaps you intended to use `graph.add`?
    y=<Tensor: name="tensor_#1", operation_name="tensor", shape=()>
    type(y)='Tensor'
    """
    advice = ""
    if alternatives is not None:
        advice = f" Perhaps you intended to use {alternatives}?"

    def _no_graph_parameters(function: Callable):
        arg_names = list(inspect.signature(function).parameters)

        error_message = (
            f"The parameters of `{function.__name__}` cannot be graph objects." + advice
        )

        @wraps(function)
        def _function(*args, **kwargs):
            for arg_name, arg in zip(arg_names, args):
                check_argument(
                    not isinstance(arg, NodeData),
                    error_message,
                    {arg_name: arg},
                    extras={f"type({arg_name})": type(arg).__name__},
                )

            for key, kwarg in kwargs.items():
                check_argument(
                    not isinstance(kwarg, NodeData),
                    error_message,
                    {key: kwarg},
                    extras={f"type({key})": type(kwarg).__name__},
                )
            return function(*args, **kwargs)

        return _function

    return _no_graph_parameters


def extract_graph_output(item):
    """
    Convert a non-batched item from a qctrl.types.graph/optimization.Result.output
    dictionary into a NumPy array.

    If the item is a dictionary (corresponds to a tensor), then its "value" is returned.

    If the item is a list of dictionaries (corresponds to a Pwc), then the "value"
    elements of its inner dictionaries are returned in a NumPy array.

    Parameters
    ----------
    item : dict or list
        The item of a Result.output dictionary representing a tensor or a PWC node.

    Returns
    -------
    np.ndarray or number
        The value of the tensor node or the values of the PWC node.
    """
    if isinstance(item, dict):
        return item["value"]
    if isinstance(item, list):
        assert all(
            isinstance(elem, dict) for elem in item
        ), "Batches are not supported."
        return np.array([seg["value"] for seg in item])
    assert False, "Unknown output format."
