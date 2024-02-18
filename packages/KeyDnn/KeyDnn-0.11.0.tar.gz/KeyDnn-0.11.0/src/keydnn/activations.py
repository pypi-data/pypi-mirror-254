from typing import *

import numpy as np

from keydnn.utilities import ComplexFunction

class Activation(ComplexFunction):

    ACTIVATION_FUNCTIONS = {}

    ACTIVATION_COUNTER = 1

    __DEFAULT = None

    @classmethod
    def contains_activation_layer(cls, name : str) -> bool:

        if (cls.DEBUG_MODE):
            assert isinstance(name, str)

        return cls.ACTIVATION_FUNCTIONS.__contains__(name.lower())

    @classmethod
    def get_activation_layer(cls, name : str, default_value : Optional[ Any ] = __DEFAULT) -> "Activation":

        if (cls.DEBUG_MODE):
            assert isinstance(name, str)

        if (default_value is cls.__DEFAULT):
            return cls.ACTIVATION_FUNCTIONS[name.lower()]
        
        return cls.ACTIVATION_FUNCTIONS.get(name.lower(), default_value)

    @classmethod
    def _add_activation_instance(cls, name : str, target_instance : "Activation") -> None:

        if (cls.DEBUG_MODE):
            assert isinstance(target_instance, Activation)

        if (name == ""):
            raise ValueError("Activation layer name cannot be empty")

        if (name in cls.ACTIVATION_FUNCTIONS):
            raise KeyError(f"Activation layer name collision. The following name already exists: `{name}`")

        cls.ACTIVATION_FUNCTIONS[name] = target_instance

    @classmethod
    def __generate_instance_name(cls) -> str:

        instance_name = f"unknown_activation_function_{cls.ACTIVATION_COUNTER}"

        cls.ACTIVATION_COUNTER += 1

        return instance_name

    def __init__(self, function   : Optional[ Callable ] = None,
                       derivative : Optional[ Callable ] = None,
                       inference  : Optional[ Callable ] = None,
                       gradient   : Optional[ Callable ] = None, *,
                       name       : Optional[ str ]      = None) -> None:

        if (self.DEBUG_MODE):

            assert ((name is None) or (isinstance(name, str)))

            assert ((gradient is None) or (callable(gradient)))

        self.name = ((self.__generate_instance_name()) if (name is None) else (name.lower()))

        self._gradient = gradient

        self.__gradient_self_ref = True

        super(Activation, self).__init__(function, derivative, inference)

        self._add_activation_instance(self.name, self)

        if (self._gradient is not None):
            self.__gradient_self_ref = False

    def define_gradient(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._gradient = target_function

    def apply_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._gradient is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_gradient`.")

        if (self.__gradient_self_ref):
            return self._gradient(self, x, gradient, *args, **kwargs)

        return self._gradient(x, gradient, *args, **kwargs)

Sigmoid = sigmoid = Activation(name = "sigmoid")

@Sigmoid.define_function
def _sigmoid_function(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    positive_mask = (x >= 0)
    
    positive = 1.0 / (1.0 + np.exp(- x * positive_mask))

    negative = np.exp(x * (x < 0))

    negative = negative / (1.0 + negative)
    
    return np.where(positive_mask, positive, negative)

@Sigmoid.define_derivative
def _sigmoid_derivative(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    value = self.call_function(x)

    return value * (1 - value)

@Sigmoid.define_gradient
def _sigmoid_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(gradient, np.ndarray)

    value = self.call_derivative(x)

    return value * gradient

@Sigmoid.define_inference
def _sigmoid_inference(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return self.call_function(x)

ReLU = relu = Activation(name = "relu")

@ReLU.define_function
def _relu_function(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return np.maximum(0, x)

@ReLU.define_derivative
def _relu_derivative(self, x : np.ndarray, *args) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return np.float32(x > 0)

@ReLU.define_gradient
def _relu_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(gradient, np.ndarray)

    value = self.call_derivative(x)

    return value * gradient

@ReLU.define_inference
def _relu_inference(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return self.call_function(x)

TanH = tanh = Activation(name = "tanh")

@TanH.define_function
def _tanh_function(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    positive_mask = (x >= 0)

    positive = ((2.0) / (1 + np.exp(-2 * (x * positive_mask))) - 1.0)

    negative = np.exp(2.0 * x * (x < 0))

    negative = (negative - 1.0) / (negative + 1.0)

    return np.where(positive_mask, positive, negative)

@TanH.define_derivative
def _tanh_derivative(self, x : np.ndarray, *args) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return (1 - np.power(self.call_function(x), 2))

@TanH.define_gradient
def _tanh_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(gradient, np.ndarray)

    value = self.call_derivative(x)

    return value * gradient

@TanH.define_inference
def _tanh_inference(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return self.call_function(x)

Softmax = softmax = Activation(name = "softmax")

@Softmax.define_function
def _softmax_function(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    y = np.exp(x - np.max(x, axis = -1, keepdims = True))

    return y / np.sum(y, axis = -1, keepdims = True)

@Softmax.define_derivative
def _softmax_derivative(self, x : np.ndarray, *args) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    # (B, O)
    softmax = self.call_function(x)

    (B, O) = softmax.shape

    # (B, O, O)
    jacobian_1 = np.einsum("BOQ,BQ->BOQ", np.identity(O).reshape((1, O, O)).repeat(B, axis = 0), softmax, optimize = True)

    # (B, O, O)
    jacobian_2 = np.einsum("BO,BQ->BOQ", softmax, softmax, optimize = True)

    # (B, O, O)
    jacobian = jacobian_1 - jacobian_2

    return jacobian

@Softmax.define_gradient
def _softmax_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(gradient, np.ndarray)
        
    # (B, O, O)
    jacobian = self.call_derivative(x)

    return np.einsum("BOQ,BQ->BO", jacobian, gradient, optimize = True)

@Softmax.define_inference
def _softmax_inference(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return self.call_function(x)

LeakyReLU = leaky_relu = Activation(name = "leaky_relu")

leaky_relu_alpha = 0.02

@LeakyReLU.define_function
def _leaky_relu_function(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return np.where((x > 0), (x), (x * leaky_relu_alpha))

@LeakyReLU.define_derivative
def _leaky_relu_derivative(self, x : np.ndarray, *args) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    ones = np.ones_like(x)

    return np.where((x > 0), ones, ones * leaky_relu_alpha)

@LeakyReLU.define_gradient
def _leaky_relu_gradient(self, x : np.ndarray, gradient : np.ndarray, *args, **kwargs) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(gradient, np.ndarray)

    value = self.call_derivative(x)

    return value * gradient

@LeakyReLU.define_inference
def _leaky_relu_inference(self, x : np.ndarray) -> np.ndarray:

    if (self.DEBUG_MODE):
        assert isinstance(x, np.ndarray)

    return self.call_function(x)

if (__name__ == "__main__"):

    print(Activation.ACTIVATION_FUNCTIONS)

    test_classes = [ TanH, Sigmoid, ReLU, sigmoid, relu, tanh, softmax ]

    for test_class in test_classes:

        test_data = np.array([ [ 600, 1, 2, 3, 4, 500 ], [ 2, 2, 2, 2, 2, 2 ] ])

        test_output = test_class.call_function(test_data)

        print(test_output.shape)

        print(test_output)

        test_output = test_class.call_derivative(test_data)

        print(test_output.shape)

        print(test_output)

        test_output = test_class.call_inference(test_data)

        print(test_output.shape)

        print(test_output)

        test_output = test_class(test_data)

        print(test_output.shape)

        print(test_output)