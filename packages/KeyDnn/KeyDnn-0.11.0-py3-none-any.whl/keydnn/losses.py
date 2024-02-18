from keydnn.utilities import ComplexFunction

from keydnn.utilities import epsilon

from typing import *

import numpy as np 

class Loss(ComplexFunction):

    LOSS_FUNCTIONS = {}

    LOSS_COUNTER = 1

    __DEFAULT = None

    @classmethod
    def contains_loss_function(cls, name : str) -> bool:

        if (cls.DEBUG_MODE):
            assert isinstance(name, str)

        return cls.LOSS_FUNCTIONS.__contains__(name.lower())

    @classmethod
    def get_loss_function(cls, name : str, default_value : Optional[ Any ] = __DEFAULT) -> "Loss":

        if (cls.DEBUG_MODE):
            assert isinstance(name, str)

        if (default_value is cls.__DEFAULT):
            return cls.LOSS_FUNCTIONS[name.lower()]
        
        return cls.LOSS_FUNCTIONS.get(name.lower(), default_value)

    @classmethod
    def _add_loss_instance(cls, name : str, target_instance : "Loss") -> None:

        if (cls.DEBUG_MODE):
            assert isinstance(target_instance, Loss)

        if (name == ""):
            raise ValueError("Loss function name cannot be empty")

        if (name in cls.LOSS_FUNCTIONS):
            raise KeyError(f"Loss function name collision. The following name already exists: `{name}`")

        cls.LOSS_FUNCTIONS[name] = target_instance

    @classmethod
    def __generate_instance_name(cls) -> str:

        instance_name = f"unknown_loss_function_{cls.LOSS_COUNTER}"

        cls.LOSS_COUNTER += 1

        return instance_name

    def __init__(self, function   : Optional[ Callable ] = None,
                       derivative : Optional[ Callable ] = None,
                       inference  : Optional[ Callable ] = None, *,
                       is_average : Optional[ bool ]     = False,
                       name       : Optional[ str ]      = None) -> None:
        
        if (self.DEBUG_MODE):
            assert ((name is None) or (isinstance(name, str)))

        self.name = ((self.__generate_instance_name()) if (name is None) else (name.lower()))

        super(Loss, self).__init__(function, derivative, inference, is_average = is_average)

        self._add_loss_instance(self.name, self)

SumSquaredError = SSE = Loss(is_average = False, name = "sse")

@SSE.define_function
def _sse_function(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return np.square(y_pred - y_true)

@SSE.define_derivative
def _sse_derivative(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return 2.0 * (y_pred - y_true)

@SSE.define_inference
def _sse_inference(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return np.sum(self.call_function(y_true, y_pred))

MeanSquaredError = MSE = Loss(is_average = True, name = "mse")

@MSE.define_function
def _mse_function(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return np.square(y_pred - y_true)

@MSE.define_derivative
def _mse_derivative(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return 2.0 * (y_pred - y_true)

@MSE.define_inference
def _mse_inference(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    sum_axes = tuple(range(1, len(np.shape(y_true))))

    return np.average(np.sum(self.call_function(y_true, y_pred), axis = sum_axes), axis = 0)

CategoricalCrossEntropy = CCE = Loss(is_average = True, name = "cce")

@CCE.define_function
def _cce_function(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return - np.sum(y_true * np.log(np.clip(y_pred, epsilon, 1 - epsilon)), axis = -1, keepdims = True)

@CCE.define_derivative
def _cce_derivative(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    return - y_true / np.clip(y_pred, epsilon, 1 - epsilon)

@CCE.define_inference
def _cce_inference(self, y_true : np.ndarray, y_pred : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):

        assert isinstance(y_true, np.ndarray)

        assert isinstance(y_pred, np.ndarray)

    sum_axes = tuple(range(1, len(np.shape(y_true))))

    return np.average(np.sum(self.call_function(y_true, y_pred), axis = sum_axes), axis = 0)

if (__name__ == "__main__"):

    import tensorflow as tf

    from keydnn.activations import Softmax

    y_true = np.array([ [ 0, 0, 0, 1, 0 ] ])

    y_pred = np.array([ [ -0.5, -0.2, 0.1, 0.05, -0.15 ] ])

    print(tf.keras.activations.softmax(tf.constant(y_pred)))

    print(Softmax.call_inference(y_pred), np.sum(Softmax.call_inference(y_pred)))

    cross_entropy = tf.keras.losses.categorical_crossentropy(y_true, y_pred)

    print(cross_entropy)

    output = CCE.call_function(y_true, y_pred)

    print(output)

    output = CCE.call_derivative(y_true, y_pred)

    print(output)

    output = CCE.call_inference(y_true, y_pred)

    print(output)

    output = CCE(y_true, y_pred)

    print(output)

