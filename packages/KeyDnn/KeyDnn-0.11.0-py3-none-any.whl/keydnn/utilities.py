from typing import *

import numpy as np

import inspect

import base64

import re

def bytes2string(bytes : bytes, encoding : str = "ascii") -> str:

    return base64.b64encode(bytes).decode(encoding)

def string2bytes(base64_string : str) -> bytes:

    return base64.b64decode(base64_string)

class OptimizableClass(object):

    DEBUG_MODE = True

    @classmethod
    def optimize(cls) -> None:

        # disable debug mode
        cls.DEBUG_MODE = False

class ComplexFunction(OptimizableClass):

    def __init__(self, function   : Optional[ Callable ] = None,
                       derivative : Optional[ Callable ] = None,
                       inference  : Optional[ Callable ] = None, *,
                       is_average : Optional[ bool ]     = False) -> None:

        if (self.DEBUG_MODE):

            assert ((function is None) or (callable(function)))

            assert ((derivative is None) or (callable(derivative)))

            assert ((inference is None) or (callable(inference)))

            assert ((isinstance(is_average, bool)) or (isinstance(is_average, int)))

        # whether to pass object reference on inference for activation function and its derivative

        self.__function_self_ref   = True

        self.__derivative_self_ref = True

        self.__inference_self_ref  = True

        self.__is_average          = is_average

        # save reference to activation function and its derivative

        self._function   = function

        self._derivative = derivative

        self._inference  = inference

        # setting the object reference flags to False if function specified

        if (self._function is not None):
            self.__function_self_ref = False

        if (self._derivative is not None):
            self.__derivative_self_ref = False

        if (self._inference is not None):
            self.__inference_self_ref = False

    def define_function(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._function = target_function

    def define_derivative(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._derivative = target_function

    def define_inference(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._inference = target_function

    def call_function(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._function is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_function`.")

        if (self.__function_self_ref):
            return self._function(self, x, *args, **kwargs)

        return self._function(x, *args, **kwargs)

    def call_derivative(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._derivative is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_derivative`.")

        if (self.__derivative_self_ref):
            return self._derivative(self, x, *args, **kwargs)

        return self._derivative(x, *args, **kwargs)

    def call_inference(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._inference is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_inference`.")

        if (self.__inference_self_ref):
            return self._inference(self, x, *args, **kwargs)

        return self._inference(x, *args, **kwargs)
    
    def merge_losses(self, losses        : Iterable[ Union[ float, int ] ], 
                           sample_counts : Iterable[ int ]
            
            ) -> Tuple[ float, int ]:

        if (self.DEBUG_MODE):

            assert ((isinstance(losses, list)) or (isinstance(losses, tuple)) or (isinstance(losses, np.ndarray)))

            assert ((isinstance(sample_counts, list)) or (isinstance(sample_counts, tuple)) or (isinstance(sample_counts, np.ndarray)))

            assert (len(losses) == len(sample_counts))

        total_samples = int(np.sum(sample_counts))

        if (self.__is_average):
            return (float(np.dot(losses, sample_counts) / total_samples), total_samples)
        
        return (float(np.sum(losses)), total_samples)

    def __call__(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        return self.call_inference(x, *args, **kwargs)
    

class NetworkLayer(OptimizableClass):
    pass

class NeuralNetwork(OptimizableClass):

    NETWORK_LAYERS = {}

    @classmethod
    def register_layer(cls, layer_class : Type[ "NetworkLayer" ]) -> Type[ "NetworkLayer" ]:

        cls.NETWORK_LAYERS[layer_class.__name__] = layer_class

        return layer_class
    
def batch_one_hot_encode(indices : np.ndarray, num_classes : Optional[ int ] = 10) -> np.ndarray:

    batch_size : int = len(indices)

    encoded_matrix : np.ndarray = np.zeros((batch_size, num_classes))

    for i in range(batch_size):
        encoded_matrix[i, indices[i]] = 1

    return encoded_matrix

def catch_error(default_value : Optional[ Any ] = None, ignore : Optional[ List[ Exception ] ] = []) -> Callable:

    ignore_tuple : Exception = tuple([  KeyboardInterrupt, *ignore  ])

    def _catch_error(function : Callable) -> Callable:

        def __catch_error(*args, **kwargs) -> Any:

            try:
                return function(*args, **kwargs)

            except ignore_tuple:
                raise

            except Exception:
                return default_value
            
        return __catch_error
    
    return _catch_error

def initialize_weights(target_size : tuple, n_input_nodes : int) -> np.ndarray:
    return np.random.randn(*target_size).reshape(target_size) * np.sqrt(2.0 / n_input_nodes)

class NeoVisUtils(object):

    SAFE_MODE = True

    @classmethod
    def apply_filter_condition(cls, f_query_string : str, condition : Dict[ str, str ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(f_query_string, str)

            assert isinstance(condition, dict)

        return f_query_string.format(f"""{{{  ",".join(map(lambda x : f"{x[0]}: {repr(x[1])}", condition.items()))  }}}""")

    @classmethod
    def create_node_query_string(cls, counter : int, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(counter, int)

            assert isinstance(query_data, list)

        if (counter == 1):
            return f"p{counter} = (n{counter}: `{query_data[counter-1][0]}`{{}})"

        return f"p{counter} = (n{counter}) - [r{counter}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})"

    @classmethod
    def format_query(cls, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):
            assert isinstance(query_data, list)

        query_string = cls.apply_filter_condition(f"MATCH {cls.create_node_query_string(1, query_data)}", query_data[0][1])

        for counter in range(2, len(query_data) + 1):
            query_string += cls.apply_filter_condition(f" OPTIONAL MATCH p{counter} = (n{counter-1}) - [r{counter-1}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})", query_data[counter-1][1])

        query_string += " RETURN " + ", ".join(f"p{counter}" for counter in range(1, len(query_data) + 1))

        return query_string

epsilon = 1e-7

class ChineseDigitsConverter(object):

    SINGLE_DIGITS = "零一二三四五六七八九"

    DIGIT_UNITS = "十百千萬億兆"

    SINGLE_DIGITS_MAP = {
        "零" : 0,
        "一" : 1,
        "二" : 2,
        "三" : 3,
        "四" : 4,
        "五" : 5,
        "六" : 6,
        "七" : 7,
        "八" : 8,
        "九" : 9,
        "兩" : 2
    }

    UNITS_WEIGHTS = [
        10, 100, 1_000, 10_000, 100_000_000, 1_000_000_000_000
    ]

    @staticmethod
    def find_number_clusters(int_array : List[ int ]) -> List[ int ]:

        indices = []
        
        cur_idx = 0
        
        num_idx = len(int_array)

        while (cur_idx < num_idx):
            
            max_idx = max(range(cur_idx, num_idx), key = int_array.__getitem__)

            indices.append(max_idx)

            cur_idx = max_idx + 1

        return indices 

    @classmethod
    def _zh2no(cls, word : str) -> str:
        return "".join(map(lambda x : str(cls.SINGLE_DIGITS.index(x)), word))

    @classmethod
    def _convert_to_integer(cls, string_list : List[ str ]) -> int:

        last_item = string_list[-1]

        if (len(last_item) == 1):
            
            if (cls.DIGIT_UNITS.__contains__(last_item)):
                multiplier = cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(last_item)]
                last_digit = -1

            else:
                multiplier = 1
                last_digit = cls.SINGLE_DIGITS_MAP[last_item]

        else:

            multiplier = cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(last_item[1])]

            last_digit = cls.SINGLE_DIGITS_MAP[last_item[0]]

        accumulation = 0

        for string in string_list[:-1]:

            if ((len(string) == 1) and (string == "零")):
                continue

            digit, units = cls.SINGLE_DIGITS_MAP[string[0]], cls.UNITS_WEIGHTS[cls.DIGIT_UNITS.index(string[1])]

            accumulation += (digit * units)

        return multiplier * ((accumulation + last_digit) if (last_digit != -1) else max(1, accumulation))

    @classmethod
    def _process(cls, word : str) -> str:

        tokens = list(filter("".__ne__, re.findall(f"[{cls.SINGLE_DIGITS}兩]?[{cls.DIGIT_UNITS}]?", word)))

        unit_indices = [
            ((cls.DIGIT_UNITS.index(x[-1])) if (cls.DIGIT_UNITS.__contains__(x[-1])) else (-2))
                for x in tokens
        ]

        clusters = cls.find_number_clusters(unit_indices)

        accumulation = 0

        for idx, start_idx in enumerate(clusters):

            actual_start_idx = ((0) if (idx == 0) else (clusters[idx-1] + 1))

            accumulation += cls._convert_to_integer(tokens[actual_start_idx:start_idx+1])

        return str(accumulation)

    @classmethod
    def chinese_to_arabic(cls, sentence : str) -> str:

        assert isinstance(sentence, str)

        patt = f"[{cls.SINGLE_DIGITS}{cls.DIGIT_UNITS}兩]+"
        
        tokens = re.findall(f"{patt}|[^{cls.SINGLE_DIGITS}{cls.DIGIT_UNITS}兩]+", sentence)

        converted_tokens = []

        for token in tokens:

            if all(cls.SINGLE_DIGITS.__contains__(char) for char in token):
                converted_tokens.append(cls._zh2no(token))
                continue

            if (re.match(patt, token) is None):
                converted_tokens.append(token)
                continue

            converted_tokens.append(cls._process(token))

        return "".join(converted_tokens)
    
def type_error_check(variable : Any, type_list : List[ Union[ Type, None ] ]) -> bool:

    if ((type_list.__contains__(None)) and (variable is None)):
        return False

    if ((any((__variable is callable) for __variable in type_list)) and (callable(variable))):
        return False

    for var_type in type_list:

        if ((var_type is None) or (var_type is callable)):
            continue 

        if (isinstance(variable, var_type)):
            return False

    return True

class VariableTypeError(TypeError):

    def __init__(self, variable : Any, var_name : str, type_list : List[ Union[ Type, None ] ]) -> None:

        error_message = f"Variable {repr(var_name)} should be"

        for var_type in type_list:

            if (var_type is None):
                error_message += " None,"

            elif (var_type is callable):
                error_message += " callable,"

            else:
                error_message += f" {repr(var_type)},"

        super(VariableTypeError, self).__init__(error_message[:-1] + ".")

def save_parameters(private_level : Optional[ int ] = 0) -> Callable:

    if (type_error_check(private_level, [ int ])):
        raise VariableTypeError(private_level, "private_level", [ int ])

    if (private_level < 0):
        raise ValueError(f"""Parameter `private_level` cannot be a negative number.""")

    def get_default_args(function : Callable) -> Dict[ str, any ]:

        return {
            key : val.default 
                for key, val in inspect.signature(function).parameters.items()
                    if val.default is not inspect.Parameter.empty
        }

    def _set_variables(self, init_function : Callable, *args, **kwargs) -> None:

        nonlocal private_level, get_default_args

        class_prefix = ((f"_{self.__class__.__name__}") if (private_level >= 2) else (""))

        prefix = "_" * private_level

        for key, val in get_default_args(init_function).items():
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

        for key, val in kwargs.items():
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

        for key, val in zip(init_function.__code__.co_varnames[1:], args):
            setattr(self, f"""{class_prefix}{prefix}{key}""", val)

    def _save_parameters(init_function : Callable) -> Callable:

        nonlocal _set_variables

        if (type_error_check(init_function, [ callable ])):
            raise VariableTypeError(init_function, "init_function", [ callable ])

        def __save_parameters(self, *args, **kwargs) -> None:

            nonlocal _set_variables, init_function

            _set_variables(self, init_function, *args, **kwargs)

            init_function(self, *args, **kwargs)

        return __save_parameters

    return _save_parameters

class KeyResponse(dict):

    def __check_type(self) -> None:

        if (type_error_check(self.__status, [ bool ])):
            raise VariableTypeError(self.__status, "status", [ bool ])

        if (type_error_check(self.__info, [ str ])):
            raise VariableTypeError(self.__info, "info", [ str ])

    @save_parameters(2)
    def __init__(self, status : bool, message : Any, info : Optional[ str ] = "", **kwargs) -> None:

        super(KeyResponse, self).__init__()

        self.__check_type()

        self.update({
            "status"  : status,
            "message" : message
        })

        if (info != ""):
            self.__setitem__("info", info)

        self.update(kwargs)

if (__name__ == "__main__"):

    @catch_error()
    def parse_int(string : str) -> int:
        return int(string)
    
    print(parse_int("123"))

    print(parse_int("2-3"))