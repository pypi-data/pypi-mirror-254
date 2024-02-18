from typing import *

from keydnn.utilities import bytes2string, string2bytes

from keydnn.utilities import NetworkLayer, NeuralNetwork

from keydnn.utilities import initialize_weights

from keydnn.activations import Activation

from keydnn.conv_utils import ConvTools

import numpy as np 

class V1NetworkLayer(NetworkLayer):
        
    def __init__(self, *args, **kwargs) -> None:
        pass

    def clear_gradients(self) -> None:
        pass

    def optimize(self, *args, **kwargs) -> None:
        pass

    def get_weights(self) -> None:
        return None

    def without_gradients(self) -> None:
        pass

    def use_gradients(self) -> None:
        pass

    def forward(self, *args, **kwargs) -> None:
        raise NotImplementedError("The forward function has not been implemented.")

    def backward(self, *args, **kwargs) -> None:
        raise NotImplementedError("The backward function has not been implemented.")

@NeuralNetwork.register_layer
class Linear(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "Linear") -> Dict[ str, Union[ str, int, bytes ] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, Linear)

        output_data = {
            "weights" : {
                "W" : bytes2string(layer._W.tobytes()),
                "B" : bytes2string(layer._B.tobytes())
            },
            "shape" : {
                "I" : layer._input_size,
                "O" : layer._output_size
            },
            "dtype" : {
                "W" : layer._W.dtype.str,
                "B" : layer._B.dtype.str
            },
            "activation" : {
                "A" : (("") if (layer._activation is None) else (layer._activation.name))
            }
        }

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int, bytes ] ]) -> "Linear":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        linear_layer = Linear(
            input_size  = layer_data["shape"]["I"],
            output_size = layer_data["shape"]["O"],
            activation  = Activation.get_activation_layer(layer_data["activation"]["A"], None)
        )

        linear_layer._W = np.reshape(
            np.frombuffer(string2bytes(layer_data["weights"]["W"]), dtype = layer_data["dtype"]["W"]),
            (layer_data["shape"]["O"], layer_data["shape"]["I"])
        )

        linear_layer._B = np.reshape(
            np.frombuffer(string2bytes(layer_data["weights"]["B"]), dtype = layer_data["dtype"]["B"]),
            (layer_data["shape"]["O"], 1)
        )

        return linear_layer

    def __init__(self, input_size  : int,
                       output_size : int,
                       activation  : Optional[ Union[ Activation, str ] ] = None) -> None:
        
        super(Linear, self).__init__()

        if (self.DEBUG_MODE):

            assert isinstance(input_size, int)

            assert isinstance(output_size, int)

            assert ((activation is None) or (isinstance(activation, Activation)) or (isinstance(activation, str)))

            assert input_size > 0

            assert output_size > 0

        # basic parameters

        self._input_size  = input_size

        self._output_size = output_size

        self._activation  = activation

        if (isinstance(self._activation, str)):

            if not (Activation.contains_activation_layer(self._activation)):
                raise KeyError(f"The name of the following activation layer could not be found: `{self._activation}`")
            
            self._activation = Activation.get_activation_layer(self._activation)

        # layer weights and biases

        self._W = initialize_weights((self._output_size, self._input_size), self._input_size)

        self._B = np.zeros(shape = (self._output_size, 1)) #initialize_weights((self._output_size, 1), self._input_size)

        # optimizer parameters : temporary values and gradients

        self._W_gradients = np.zeros_like(self._W)

        self._B_gradients = np.zeros_like(self._B)

        self._track_grads = True

        self._X = None

        self._Z = None

        self._A = None

    def clear_gradients(self) -> None:

        self._W_gradients.fill(0)

        self._B_gradients.fill(0)

    def optimize(self, learning_rate   : Optional[ Union[ float, int ] ] = 0.001, *,
                       clear_gradients : Optional[ bool ] = False) -> None:

        if (self.DEBUG_MODE):

            assert ((isinstance(learning_rate, float)) or (isinstance(learning_rate, int)))

            assert learning_rate > 0

        if (self._track_grads == False):
            raise Warning("Optimizing model weights without tracking gradients. Consider enabling gradients by calling `use_gradients`.")

        # update weights and biases

        self._W -= (learning_rate * self._W_gradients)

        self._B -= (learning_rate * self._B_gradients)

        # clear gradients if specified by engineer

        if (clear_gradients):
            self.clear_gradients()

    def get_weights(self) -> Tuple[ np.ndarray, np.ndarray ]:

        return (self._W.copy(), self._B.copy())

    def without_gradients(self) -> None:

        # should not track gradients
        self._track_grads = False

    def use_gradients(self) -> None:

        # should track gradients
        self._track_grads = True

    def forward(self, x : np.ndarray) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        # (B, O) <= (O, I) x (B, I) + (B, O)
        Z = np.einsum("OI,BI->BO", self._W, x, optimize = True) + self._B.T

        # (B, O)
        A = Z

        if (self._activation is not None):

            # (B, O)
            A = self._activation.call_function(Z)

        # should track temporary values for back propagation

        if (self._track_grads):

            # (B, I)
            self._X = x.copy()

            # (B, O)
            self._Z = Z

            # (B, O)
            self._A = A

        else:

            self._X = None

            self._Z = None

            self._A = None

        return A

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, O)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        if (self._track_grads == False):
            raise ValueError("Back propagation without gradients is forbidden. Try enabling gradients by calling `use_gradients`.")

        if (any((x is None) for x in [ self._X, self._Z, self._A ])):
            raise ValueError("Back propagation before forward propagation is forbidden. Try calling `forward` first.")

        # Z Formula : [ Z = WX + B : (O, 1) = (O, I) x (I, 1) ]

        # (O, 1) : initialized with ones
        dZ_dB = np.ones_like(self._B)


        # (B, O) : initialize ones-matrix if activation is undefined
        # dA_dZ = np.ones_like(gradient)

        # (B, O) <= (B, O) * (B, O)
        dZ = gradient

        if (self._activation is not None):

            # (B, O) : partial derivative of activation with respect to Z
            # dA_dZ = self._activation.call_derivative(self._Z)

            # (B, O) : (B, O) * (B, O) or (B, O) x (B, O, O)
            # dZ = self._activation.call_derivative(self._Z, gradient)

            # (B, O)
            dZ = self._activation.apply_gradient(self._Z, gradient)

        # (B, O) <= (B, O) * (B, O)
        # dZ = gradient * dA_dZ


        # (O, 1) <= (O,) <= (B, O) <= (B, O) x (1, O)
        dB = np.reshape(np.sum(dZ * dZ_dB.T, axis = 0), (self._output_size, 1))

        # (O, I) <= (B, O, I) <= (B, O) x (B, I)
        dW = np.sum(np.einsum("BO,BI->BOI", dZ, self._X, optimize = True), axis = 0)

        # (B, I) <= (O, I) x (B, O)
        dX = np.einsum("OI,BO->BI", self._W, dZ, optimize = True)

        # (O, 1) <= (O, 1) + (O, 1)
        self._B_gradients += dB

        # (O, I) <= (O, I) + (O, I)
        self._W_gradients += dW

        return dX

@NeuralNetwork.register_layer
class Conv2D(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "Conv2D") -> Dict[ str, Union[ str, int, bytes ] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, Conv2D)

        output_data = {
            "weights" : {
                "W" : bytes2string(layer._W.tobytes()),
                "B" : bytes2string(layer._B.tobytes())
            },
            "shape" : {
                "C"  : layer._input_channels,
                "CC" : layer._output_channels,
                "CH" : layer._kernel_height,
                "CW" : layer._kernel_width,
                "SH" : layer._strides[0],
                "SW" : layer._strides[1]
            },
            "dtype" : {
                "W" : layer._W.dtype.str,
                "B" : layer._B.dtype.str
            },
            "activation" : {
                "A" : (("") if (layer._activation is None) else (layer._activation.name))
            }
        }

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int, bytes ] ]) -> "Conv2D":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        conv_layer = Conv2D(
            input_channels  = layer_data["shape"]["C"],
            output_channels = layer_data["shape"]["CC"],
            kernel_size     = (layer_data["shape"]["CH"], layer_data["shape"]["CW"]),
            strides         = (layer_data["shape"]["SH"], layer_data["shape"]["SW"]),
            activation      = Activation.get_activation_layer(layer_data["activation"]["A"], None)
        )

        # (CC, C, CH, CW)

        conv_layer._W = np.reshape(
            np.frombuffer(string2bytes(layer_data["weights"]["W"]), dtype = layer_data["dtype"]["W"]),
            (layer_data["shape"]["CC"], layer_data["shape"]["C"], layer_data["shape"]["CH"], layer_data["shape"]["CW"])
        )

        # (CC, 1)

        conv_layer._B = np.reshape(
            np.frombuffer(string2bytes(layer_data["weights"]["B"]), dtype = layer_data["dtype"]["B"]),
            (layer_data["shape"]["CC"], 1)
        )

        return conv_layer
        
    def __init__(self, input_channels  : int,
                       output_channels : int,
                       kernel_size     : Union[ int, Tuple[ int, int ] ],
                       strides         : Optional[ Union[ int, Tuple[ int, int ] ] ] = 1,
                       activation      : Optional[ Union[ str, Activation ] ] = None, *,
                       num_workers     : Optional[ int ] = 4
                       
                ) -> None:
        
        super(Conv2D, self).__init__()
        
        if (self.DEBUG_MODE):

            assert isinstance(input_channels, int)

            assert isinstance(output_channels, int)

            assert ((isinstance(kernel_size, int)) or (isinstance(kernel_size, tuple)))

            assert ((isinstance(strides, int)) or (isinstance(strides, tuple)))

            assert ((activation is None) or (isinstance(activation, Activation)) or (isinstance(activation, str)))

            assert isinstance(num_workers, int)

            assert input_channels > 0

            assert output_channels > 0

            assert num_workers > 0

            if (isinstance(strides, int)):
                assert strides > 0

            if (isinstance(kernel_size, int)):
                assert kernel_size > 0

        if (isinstance(kernel_size, int)):
            kernel_size = (kernel_size, kernel_size)

        if (isinstance(strides, int)):
            strides = (strides, strides)

        # basic parameters

        # (C)
        self._input_channels  = input_channels

        # (CC)
        self._output_channels = output_channels

        # (CH, CW)
        self._kernel_size     = kernel_size

        # (SH, SW)
        self._strides         = strides

        # :)
        self._activation      = activation

        # (CH)
        self._kernel_height   = self._kernel_size[0]

        # (CW)
        self._kernel_width    = self._kernel_size[1]

        self._num_workers     = num_workers

        if (isinstance(self._activation, str)):

            if not (Activation.contains_activation_layer(self._activation)):
                raise KeyError(f"The name of the following activation layer could not be found: `{self._activation}`")
            
            self._activation = Activation.get_activation_layer(self._activation)

        # layer weights and biases
            
        N = np.prod((self._input_channels, self._kernel_height, self._kernel_width))

        # (CC, C, CH, CW)
        self._W = initialize_weights((self._output_channels, self._input_channels, self._kernel_height, self._kernel_width), N)

        # (CC, 1)
        self._B = np.zeros(shape = (self._output_channels, 1)) #initialize_weights((self._output_channels, 1), N)

        # optimizer parameters : temporary values and gradients

        # (CC, C, CH, CW)
        self._W_gradients = np.zeros_like(self._W)

        # (CC, C, 1)
        self._B_gradients = np.zeros_like(self._B)

        # whether to track gradients and temporary variables
        self._track_grads = True

        self._X = None

        self._Z = None

        self._A = None

    def clear_gradients(self) -> None:

        self._W_gradients.fill(0)

        self._B_gradients.fill(0)

    def optimize(self, learning_rate   : Optional[ Union[ float, int ] ] = 0.001, *,
                       clear_gradients : Optional[ bool ] = False) -> None:

        if (self.DEBUG_MODE):

            assert ((isinstance(learning_rate, float)) or (isinstance(learning_rate, int)))

            assert learning_rate > 0

        if (self._track_grads == False):
            raise Warning("Optimizing model weights without tracking gradients. Consider enabling gradients by calling `use_gradients`.")

        # update weights and biases

        self._W -= (learning_rate * self._W_gradients)

        self._B -= (learning_rate * self._B_gradients)

        # clear gradients if specified by engineer

        if (clear_gradients):
            self.clear_gradients()

    def get_weights(self) -> Tuple[ np.ndarray, np.ndarray ]:

        return (self._W.copy(), self._B.copy())

    def without_gradients(self) -> None:

        # should not track gradients
        self._track_grads = False

    def use_gradients(self) -> None:

        # should track gradients
        self._track_grads = True

    def forward(self, x : np.ndarray) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        (*_, self.__H, self.__W) = x.shape

        # x : (B, C, H, W)

        # (OH) = (H - CH) // SH + 1
            
        # (OW) = (W - CW) // SW + 1

        # (B, CC, OH, OW) <= (B, C, H, W) x (CC, C, CH, CW) + (1, CC, 1, 1)
        Z = ConvTools.apply_convolution(
            x, 
            self._W, 
            self._strides, 
            num_workers = self._num_workers

        ) + self._B.reshape((1, self._output_channels, 1, 1))

        # (B, CC, OH, OW)
        A = Z

        if (self._activation is not None):

            # (B, CC, OH, OW)
            A = self._activation.call_function(Z)

        # should track temporary values for back propagation

        if (self._track_grads):

            # (B, C, H, W)
            self._X = x.copy()

            # (B, CC, OH, OW)
            self._Z = Z

            # (B, CC, OH, OW)
            self._A = A

        else:

            self._X = None

            self._Z = None

            self._A = None

        return A

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, CC, OH, OW)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        if (self._track_grads == False):
            raise ValueError("Back propagation without gradients is forbidden. Try enabling gradients by calling `use_gradients`.")

        if (any((x is None) for x in [ self._X, self._Z, self._A ])):
            raise ValueError("Back propagation before forward propagation is forbidden. Try calling `forward` first.")

        # (B, CC, OH, OW) : initialize ones-matrix if activation is undefined
        # dA_dZ = np.ones_like(gradient)

        dZ = gradient

        if (self._activation is not None):

            # (B, CC, OH, OW) : partial derivative of activation with respect to Z
            # dA_dZ = self._activation.call_derivative(self._Z)

            # (B, CC, OH, OW)
            dZ = self._activation.apply_gradient(self._Z, gradient)

        # (CC, 1) : initialized with ones
        dZ_dB = np.ones_like(self._B)

        # (B, CC, OH, OW) <= (B, CC, OH, OW) * (B, CC, OH, OW)
        # dZ = gradient * dA_dZ

        # (CC, 1) <= (B, CC, OH, OW) x (CC, 1)
        dB = np.reshape(np.einsum("BXHW,XO->XO", dZ, dZ_dB, optimize = True), (self._output_channels, 1))

        # (CC, C, CH, CW) <= (B, C, H, W) x (B, CC, OH, OW) x (CC, C, CH, CW)
        dW = ConvTools.transform_gradient_for_weights(self._X, dZ, self._W, self._strides, num_workers = self._num_workers)

        # (B, C, H, W) <= (B, CC, OH, OW) x (CC, C, CH, CW)
        dX = ConvTools.transform_gradient(dZ, self._W, self._strides, num_workers = self._num_workers)

        # (CC, 1) <= (CC, 1) + (CC, 1)
        self._B_gradients += dB

        # (CC, C, CH, CW) <= (CC, C, CH, CW) + (CC, C, CH, CW)
        self._W_gradients += dW

        (*_, H, W) = dX.shape

        if ((H != self.__H) or (W != self.__W)):
            dX = np.pad(dX, ((0, 0), (0, 0), (0, self.__H - H), (0, self.__W - W))).astype(dX.dtype)

        # (B, C, H, W)
        return dX

@NeuralNetwork.register_layer
class Flatten(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "Flatten") -> Dict[ str, Union[ str, int] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, Flatten)

        output_data = {
            "shape" : {
                "C" : layer._input_channels,
                "H" : layer._input_height,
                "W" : layer._input_width
            }
        }

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int ] ]) -> "Flatten":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        flatten_layer = Flatten(
            input_channels  = layer_data["shape"]["C"],
            input_height    = layer_data["shape"]["H"],
            input_width     = layer_data["shape"]["W"]
        )

        return flatten_layer
        
    def __init__(self, input_channels : int,
                       input_height   : int,
                       input_width    : int) -> None:
        
        super(Flatten, self).__init__()
        
        if (self.DEBUG_MODE):

            assert isinstance(input_height, int)
            
            assert isinstance(input_width, int)

            assert isinstance(input_channels, int)

            assert input_height > 0
            
            assert input_width > 0

            assert input_channels > 0

        # basic parameters

        # (C)
        self._input_channels = input_channels

        # (H)
        self._input_height   = input_height

        # (W)
        self._input_width    = input_width

    def clear_gradients(self) -> None:
        pass

    def optimize(self, *args, **kwargs) -> None:
        pass

    def get_weights(self) -> None:
        return None

    def without_gradients(self) -> None:
        pass

    def use_gradients(self) -> None:
        pass

    def forward(self, x : np.ndarray) -> np.ndarray:

        # x : (B, C, H, W)

        # (B, F) = (B, H * W * C) <= (B, C, H, W)
        return x.reshape((-1, self._input_height * self._input_width * self._input_channels))

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, F)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        # (B, C, H, W) <= (B, H * W * C) = (B, F)
        return gradient.reshape((-1, self._input_channels, self._input_height, self._input_width))

@NeuralNetwork.register_layer
class LazyFlatten(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "LazyFlatten") -> Dict[ str, Union[ str, int] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, LazyFlatten)

        output_data = {}

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int ] ]) -> "LazyFlatten":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        flatten_layer = LazyFlatten()

        return flatten_layer
        
    def __init__(self) -> None:
        super(LazyFlatten, self).__init__()

    def forward(self, x : np.ndarray) -> np.ndarray:

        # x : (B, C, H, W)

        (self._B, self._C, self._H, self._W) = x.shape

        # (B, F) = (B, H * W * C) <= (B, C, H, W)
        return x.reshape((self._B, self._C * self._W * self._H))

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, F)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        # (B, C, H, W) <= (B, H * W * C) = (B, F)
        return gradient.reshape((self._B, self._C, self._H, self._W))

@NeuralNetwork.register_layer
class MaxPooling2D(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "MaxPooling2D") -> Dict[ str, Union[ str, int] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, MaxPooling2D)

        output_data = {
            "shape" : {
                "PH" : layer._kernel_size[0],
                "PW" : layer._kernel_size[1]
            }
        }

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int ] ]) -> "MaxPooling2D":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        pool_layer = MaxPooling2D(
            kernel_size = (layer_data["shape"]["PH"], layer_data["shape"]["PW"])
        )

        return pool_layer
        
    def __init__(self, kernel_size : Tuple[ int, int ], *,
                       num_workers : Optional[ int ] = 4) -> None:
        
        super(MaxPooling2D, self).__init__()
        
        if (self.DEBUG_MODE):

            assert isinstance(kernel_size, tuple)

            assert isinstance(num_workers, int)

            assert num_workers > 0

        # basic parameters

        self._kernel_size = kernel_size

        self._num_workers = num_workers

    def forward(self, x : np.ndarray) -> np.ndarray:

        # x : (B, C, H, W)

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        (self._B, self._C, self._H, self._W) = x.shape

        (dst_matrix, self._bin_matrix) = ConvTools.max_pooling_2D(x, self._kernel_size, num_workers = self._num_workers)

        # (B, C, OH, OW)
        return dst_matrix

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, C, OH, OW)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        # (B, C, UH, UW)
        gradient = np.repeat(gradient, self._kernel_size[0], axis = 2).repeat(self._kernel_size[1], axis = 3)

        (*_, OH, OW) = gradient.shape

        # (B, C, H, W)
        gradient = np.pad(gradient, ((0, 0), (0, 0), (0, self._H - OH), (0, self._W - OW)))

        # (B, C, H, W) <= (B, C, H, W) x (B, C, H, W)
        gradient = gradient * self._bin_matrix

        return gradient

@NeuralNetwork.register_layer
class Dropout(V1NetworkLayer):

    @classmethod
    def export_to_dict(cls, layer : "Dropout") -> Dict[ str, Union[ str, int] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(layer, Dropout)

        output_data = {
            "dropout" : layer._ratio
        }

        return output_data

    @classmethod
    def import_from_dict(cls, layer_data : Dict[ str, Union[ str, int ] ]) -> "Dropout":

        if (cls.DEBUG_MODE):
            assert isinstance(layer_data, dict)

        dropout_layer = Dropout(
            ratio = layer_data["dropout"]
        )

        return dropout_layer
        
    def __init__(self, ratio : Union[ int, float ]) -> None:

        super(Dropout, self).__init__()
        
        if (self.DEBUG_MODE):

            assert ((isinstance(ratio, int)) or (isinstance(ratio, float)))

            assert ((ratio >= 0) and (ratio <= 1))

        # basic parameters

        self._ratio = ratio

    def forward(self, x : np.ndarray) -> np.ndarray:

        # x : (B, I)

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        # x : (B, I)
        self._dropout_mask = np.random.randn(*x.shape) <= (1 - self._ratio)

        # x : (B, I)
        return x * self._dropout_mask

    def backward(self, gradient : np.ndarray) -> np.ndarray:

        # gradient : (B, O)

        if (self.DEBUG_MODE):
            assert isinstance(gradient, np.ndarray)

        # gradient : (B, O)
        return self._dropout_mask * gradient

if (__name__ == "__main__"):

    test = 1

    if (test == 0):

        from activations import ReLU, Sigmoid

        from losses import SSE

        test_input = np.array([
            [ 0, 0 ], [ 0, 1 ], [ 1, 0 ], [ 1, 1 ]
        ])

        test_label = np.array([
            [ 1, 0 ], [ 0, 1 ], [ 0, 1 ], [ 1, 0 ]
        ])

        layer_1 = Linear(input_size = 2, output_size = 32, activation = "tanh")

        layer_2 = Linear(input_size = 32, output_size = 2, activation = "softmax")

        layer_1.without_gradients()

        layer_2.without_gradients()

        for epoch in range(2000):

            layer_1.use_gradients()

            layer_2.use_gradients()

            y_pred = layer_1.forward(test_input)

            y_pred = layer_2.forward(y_pred)

            loss_gradient = SSE.call_derivative(test_label, y_pred)

            loss_gradient = layer_2.backward(loss_gradient)

            loss_gradient = layer_1.backward(loss_gradient)

            layer_2.optimize(learning_rate = 0.1)

            layer_1.optimize(learning_rate = 0.1)

            if (epoch % 200 == 0):
                print(f"Epoch: {epoch + 1}, Loss: {SSE(test_label, y_pred)}")

        layer_1 = Linear.import_from_dict(Linear.export_to_dict(layer_1))

        layer_2 = Linear.import_from_dict(Linear.export_to_dict(layer_2))

        layer_1.without_gradients()

        layer_2.without_gradients()

        layer_output = layer_1.forward(test_input)

        layer_output = layer_2.forward(layer_output)

        print(np.argmax(layer_output, axis = 1))

        print(Linear.export_to_dict(layer_1))

    if (test == 1):

        from losses import SSE, MSE

        np.random.seed(0)

        test_data = np.random.randint(-10, 10, size = (16, 3, 28, 28))

        test_labl = np.random.randint(0, 1, size = (16, 8, 26, 26)).reshape((16, 8 * 26 * 26))

        conv_layer = Conv2D(3, 8, (3, 3), (1, 1), activation = "sigmoid")

        flat_layer = Flatten(8, 26, 26)

        for epoch in range(2000):

            output = conv_layer.forward(test_data)

            output = flat_layer.forward(output)

            gradient = MSE.call_derivative(test_labl, output)

            gradient = flat_layer.backward(gradient)

            conv_layer.backward(gradient)

            flat_layer.optimize(learning_rate = 0.001)

            conv_layer.optimize(learning_rate = 0.001)

            loss = MSE.call_inference(test_labl, output)

            if (epoch % 200 == 0):
                print(f"Epoch: {epoch + 1}, Loss: {loss:.4f}")
