import functools
import inspect
import typing
from typing import Any, Callable, Dict, List, Optional

from combo.common.params import Params
from combo.config.exceptions import RegistryException
from combo.config.registry import (Registry)
from combo.utils import ConfigurationError


def _get_method_arguments(method: Callable) -> List[str]:
    return list(inspect.signature(method).parameters.keys())


def get_matching_arguments(args: Dict[str, Any], func: Callable) -> Dict[str, Any]:
    method_args: List[str] = _get_method_arguments(func)
    return {arg_name: arg_val for arg_name, arg_val in args if arg_name in method_args}


def _resolve(values: typing.Union[Dict[str, Any], str], pass_down_parameters: Dict[str, Any] = None) -> Any:
    if isinstance(values, Params):
        values = Params.as_dict()

    if isinstance(values, list):
        return [_resolve(v, pass_down_parameters) for v in values]

    if isinstance(values, dict):
        if 'type' not in values:
            return {vn: _resolve(vv, pass_down_parameters) for vn, vv in values.items()}

        try:
            clz, constructor = Registry.resolve(values['type'])
        except RegistryException:
            raise ConfigurationError('No registered class with name ' + str(values["type"]))

        args = _resolve(values.get('parameters', {}), pass_down_parameters)
        constructor_method = getattr(clz, constructor)
        if constructor_method is None:
            raise ConfigurationError(str(clz) + ' has no constructor method with name ' + constructor)

        return clz.from_parameters(args, constructor, pass_down_parameters)

    return values


def serialize_single_value(value: Any, pass_down_parameter_names: List[str] = None) -> Any:
    pass_down_parameter_names = pass_down_parameter_names or []
    if isinstance(value, FromParameters):
        return value.serialize(pass_down_parameter_names)
    elif isinstance(value, list):
        return [serialize_single_value(v, pass_down_parameter_names) for v in value]
    elif isinstance(value, tuple):
        return tuple([serialize_single_value(v, pass_down_parameter_names) for v in value])
    elif isinstance(value, set):
        return set([serialize_single_value(v, pass_down_parameter_names) for v in value])
    elif isinstance(value, dict):
        return {k: serialize_single_value(v, pass_down_parameter_names) for k, v in value.items()}
    elif isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
        return value
    else:
        return str(value)


def register_arguments(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self_arg = args[0]
        if self_arg.constructed_args is None:
            other_args = args[1:] if len(args) > 1 else []

            parameters_to_register = {}

            arg_names = _get_method_arguments(func)

            if len(arg_names) > 1:
                for arg_name, arg_val in zip(arg_names[1:], other_args):
                    parameters_to_register[arg_name] = arg_val
                for kwarg_name, kwarg_val in kwargs.items():
                    parameters_to_register[kwarg_name] = kwarg_val

            self_arg.constructed_args = parameters_to_register
        return func(*args, **kwargs)

    return wrapper


class FromParameters:
    constructed_from: str = "__init__"
    constructed_args: Optional[Dict[str, Any]] = None

    @classmethod
    def pass_down_parameter_names(cls) -> List[str]:
        return []

    @classmethod
    def from_parameters(cls,
                        parameters: Dict[str, Any] = None,
                        constructor_method_name: str = None,
                        pass_down_parameters: Dict[str, Any] = None):
        parameters_to_call = {}
        if parameters is None:
            parameters = {}

        if pass_down_parameters is None:
            pass_down_parameters = {}

        parameters = {**parameters, **pass_down_parameters}

        if constructor_method_name is None:
            constructor_method_name = '__init__'

        constructor_method = getattr(cls, constructor_method_name)
        if constructor_method is None:
            raise ValueError('No method ' + str(constructor_method) + ' for class ' + str(cls))

        constructor_method_args = _get_method_arguments(constructor_method)

        no_pass_down = {}

        # First, resolve the parameters that are needed to be passed down
        for param_name, param_value in parameters.items():
            if param_name in cls.pass_down_parameter_names():
                resolved_value = _resolve(param_value, pass_down_parameters)
                pass_down_parameters[param_name] = resolved_value

                if param_name in constructor_method_args:
                    parameters_to_call[param_name] = resolved_value
            else:
                no_pass_down[param_name] = param_value

        for param_name, param_value in no_pass_down.items():
            # Resolve only the arguments that are in the constructor method signature
            if param_name in constructor_method_args:
                parameters_to_call[param_name] = _resolve(param_value, pass_down_parameters)

        if constructor_method_name == '__init__':
            return cls(**parameters_to_call)
        else:
            return constructor_method(**parameters_to_call)

    def _to_params(self, pass_down_parameter_names: List[str] = None) -> Dict[str, str]:
        parameters_to_serialize = self.constructed_args or {}
        pass_down_parameter_names = pass_down_parameter_names or []

        parameters_dict = {}
        for pn, param_value in parameters_to_serialize.items():
            if pn in pass_down_parameter_names:
                continue
            parameters_dict[pn] = serialize_single_value(param_value,
                                                         pass_down_parameter_names + self.pass_down_parameter_names())
        return parameters_dict

    def serialize(self, pass_down_parameter_names: List[str] = None) -> Dict[str, Any]:
        constructor_method = self.constructed_from if self.constructed_from else '__init__'
        if not getattr(self, constructor_method):
            raise ConfigurationError('Class ' + str(type(self)) + ' has no constructor method ' + constructor_method)

        return {'type': Registry.get_class_name(type(self), constructor_method),
                'parameters': self._to_params(pass_down_parameter_names)}


def resolve(parameters: Dict[str, Any], pass_down_parameters: Dict[str, Any] = None) -> Any:
    pass_down_parameters = pass_down_parameters or {}
    clz, clz_init = Registry.resolve(parameters['type'])
    return clz.from_parameters(parameters['parameters'], clz_init, pass_down_parameters)


def flatten_dictionary(d, parent_key='', sep='/'):
    """
    Flatten a nested dictionary.

    Parameters:
        d (dict): The input dictionary.
        parent_key (str): The parent key to use for recursion (default is an empty string).
        sep (str): The separator to use when concatenating keys (default is '_').

    Returns:
        dict: A flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dictionary(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten_dictionary(flat_dict, sep='/'):
    """
    Unflatten a flattened dictionary.

    Parameters:
        flat_dict (dict): The flattened dictionary.
        sep (str): The separator used in the flattened keys (default is '_').

    Returns:
        dict: The unflattened dictionary.
    """
    unflattened_dict = {}
    for key, value in flat_dict.items():
        keys = key.split(sep)
        current_level = unflattened_dict

        for k in keys[:-1]:
            current_level = current_level.setdefault(k, {})

        current_level[keys[-1]] = value

    return unflattened_dict


def override_parameters(parameters: Dict[str, Any], override_values: Dict[str, Any]) -> Dict[str, Any]:
    overriden_parameters = flatten_dictionary(parameters)
    override_values = flatten_dictionary(override_values)
    for ko, vo in override_values.items():
        #if ko in overriden_parameters:
        overriden_parameters[ko] = vo

    return unflatten_dictionary(overriden_parameters)


def override_or_add_parameters(parameters: Dict[str, Any], override_values: Dict[str, Any]) -> Dict[str, Any]:
    overriden_parameters = flatten_dictionary(parameters)
    override_values = flatten_dictionary(override_values)
    for ko, vo in override_values.items():
        overriden_parameters[ko] = vo

    return unflatten_dictionary(overriden_parameters)
