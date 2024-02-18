from typing import *

from keydnn.utilities import NeuralNetwork, NetworkLayer

from keydnn.activations import ReLU, Sigmoid, Softmax

from keydnn.layers import Linear

from keydnn.losses import Loss

import numpy as np

import json

import sys

import os

class Sequential(NeuralNetwork):

    @classmethod
    def export_to_dict(cls, network : "Sequential") -> Dict[ str, List[ dict ] ]:

        if (cls.DEBUG_MODE):
            assert isinstance(network, Sequential)

        network_data = {
            "sequential_network" : [
                {
                    "layer_type" : type(layer).__name__,
                    "layer_data" : type(layer).export_to_dict(layer)
                }

                for layer in network.layers
            ]
        }

        return network_data

    @classmethod
    def import_from_dict(cls, network_data : Dict[ str, List[ dict ] ]) -> "Sequential":

        if (cls.DEBUG_MODE):
            assert isinstance(network_data, dict)

        layer_list = [
            cls.NETWORK_LAYERS[layer_data["layer_type"]].import_from_dict(layer_data["layer_data"])
                for layer_data in network_data["sequential_network"]
        ]

        return Sequential(layer_list)

    def save_model(self, filename : str) -> None:

        if (self.DEBUG_MODE):
            assert isinstance(filename, str)

        os.makedirs(os.path.dirname(filename), exist_ok = True)

        with open(filename, mode = "w", encoding = "utf-8") as wf:
            json.dump(self.export_to_dict(self), wf, ensure_ascii = False, indent = 4)

    @classmethod
    def load_model(self, filename : str) -> "Sequential":

        if (self.DEBUG_MODE):
            assert isinstance(filename, str)

        if (os.path.isfile(filename) == False):
            raise FileNotFoundError(f"The specified filepath to the model could not be found: `{filename}`")

        with open(filename, mode = "r", encoding = "utf-8") as rf:
            return self.import_from_dict(json.load(rf))

    def __init__(self, layer_list : List[ NetworkLayer ]) -> None:

        if (self.DEBUG_MODE):
            assert isinstance(layer_list, list)

        self.layers = [
            layer for layer in layer_list
        ]

    def forward(self, x : np.ndarray) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        for layer in self.layers:
            x = layer.forward(x)

        return x

    def backward(self, loss_gradient : np.ndarray) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(loss_gradient, np.ndarray)

        for layer in reversed(self.layers):
            loss_gradient = layer.backward(loss_gradient)

        return loss_gradient

    def optimize(self, learning_rate   : Optional[ Union[ float, int ] ] = 0.001, *,
                       clear_gradients : Optional[ bool ]                = False) -> None:

        if (self.DEBUG_MODE):
            assert ((isinstance(learning_rate, float)) or (isinstance(learning_rate, int)))

        for layer in reversed(self.layers):
            layer.optimize(learning_rate, clear_gradients = clear_gradients)

    def without_gradients(self) -> None:

        for layer in self.layers:
            layer.without_gradients()

    def use_gradients(self) -> None:

        for layer in self.layers:
            layer.use_gradients()

    def train_on_batch(self, x_train       : np.ndarray,
                             y_train       : np.ndarray,
                             learning_rate : float,
                             loss_function : Loss) -> float:

        if (self.DEBUG_MODE):

            assert isinstance(x_train, np.ndarray)

            assert isinstance(y_train, np.ndarray)

            assert ((isinstance(learning_rate, int)) or (isinstance(learning_rate, float)))

            assert isinstance(loss_function, Loss)

        y_pred = self.forward(x_train)

        # loss_gradient = loss_function.call_function(y_train, y_pred) * loss_function.call_derivative(y_train, y_pred)

        self.backward(loss_function.call_derivative(y_train, y_pred))

        self.optimize(learning_rate = learning_rate, clear_gradients = True)

        return loss_function.call_inference(y_train, y_pred)
    
    def configure_workers(self, num_workers : int) -> None:

        if (self.DEBUG_MODE):

            assert isinstance(num_workers, int)

            assert num_workers > 0

        for layer in self.layers:

            if (hasattr(layer, "_num_workers")):
                
                layer._num_workers = num_workers
    
    def fit(self, x_train       : np.ndarray,
                  y_train       : np.ndarray,
                  learning_rate : float,
                  batch_size    : int,
                  epochs        : int,
                  loss_function : Union[ Loss, str ], *,
                  shuffle       : Optional[ bool ] = True,
                  verbose       : Optional[ bool ] = True) -> None:
        
        if (self.DEBUG_MODE):

            assert isinstance(x_train, np.ndarray)

            assert isinstance(y_train, np.ndarray)

            assert ((isinstance(learning_rate, float)) or (isinstance(learning_rate, int)))

            assert isinstance(batch_size, int)

            assert isinstance(epochs, int)

            assert ((isinstance(loss_function, Loss)) or (isinstance(loss_function, str)))

            assert ((isinstance(shuffle, bool)) or (isinstance(shuffle, int)))

            assert ((isinstance(verbose, bool)) or (isinstance(verbose, int)))

            assert learning_rate > 0

            assert batch_size > 0

            assert epochs > 0

        if (isinstance(loss_function, str)):

            if not (Loss.contains_loss_function(loss_function)):
                raise KeyError(f"The name of the following loss function could not be found: `{loss_function}`")
            
            loss_function = Loss.get_loss_function(loss_function)
        
        num_samples = len(y_train)

        for epoch in range(1, epochs + 1):

            losses = [];  sample_counts = []

            _indexes = np.arange(0, num_samples)

            if (shuffle):
                np.random.shuffle(_indexes)

            for start_idx in range(0, num_samples, batch_size):

                end_idx = min(num_samples, start_idx + batch_size)

                __indexes = _indexes[start_idx : end_idx]

                _x_train = x_train[__indexes]

                _y_train = y_train[__indexes]

                losses.append(self.train_on_batch(
                    x_train       = _x_train, 
                    y_train       = _y_train, 
                    learning_rate = learning_rate,
                    loss_function = loss_function
                ))

                sample_counts.append(int(end_idx - start_idx))

                if (verbose):

                    (loss_merged, sample_count_merged) = loss_function.merge_losses(losses, sample_counts)

                    losses = [ loss_merged ];  sample_counts = [ sample_count_merged ]

                    sys.stdout.write(f"\r[ Epoch: {epoch}/{epochs} ] [ Batch: {end_idx/num_samples*100:.2f}% ] [ Loss: {loss_merged:.4f} ]")

                    sys.stdout.flush()

            if (verbose):
                print()

class SimpleMLP(Sequential):

    def __init__(self, input_size  : int,
                       hidden_size : int,
                       output_size : int,
                       num_hidden  : int) -> None:

        if (self.DEBUG_MODE):

            assert isinstance(input_size, int)

            assert isinstance(hidden_size, int)

            assert isinstance(output_size, int)

            assert isinstance(num_hidden, int)

            assert input_size > 0

            assert hidden_size > 0

            assert output_size > 0

            assert num_hidden > 0

        layer_list = [
            Linear(input_size = input_size, output_size = hidden_size, activation = ReLU)
        ] + [
            Linear(input_size = hidden_size, output_size = hidden_size, activation = ReLU)
                for _ in range(num_hidden - 1)
        ] + [
            Linear(input_size = hidden_size, output_size = output_size, activation = Sigmoid)
        ]

        super(SimpleMLP, self).__init__(layer_list)

if (__name__ == "__main__"):

    from losses import SSE, MSE

    test_input = np.array([
        [ 0, 0 ], [ 0, 1 ], [ 1, 0 ], [ 1, 1 ]
    ])

    test_label = np.array([
        [ 1, 0 ], [ 0, 1 ], [ 0, 1 ], [ 1, 0 ]
    ])

    # network = SimpleMLP(2, 32, 2, 1)

    network = Sequential([
        Linear(2, 32, activation = "relu"),
        Linear(32, 32, activation = "tanh"),
        Linear(32, 2, activation = "softmax")
    ])

    # for epoch in range(1000):

    #     batch_loss = network.train_on_batch(test_input, test_label, learning_rate = 0.1, loss_function = SSE)

    #     if (epoch % 100 == 0):
    #         print(f"Epoch: {epoch+1}, Loss: {batch_loss}")

    network.fit(test_input, test_label, learning_rate = 0.1, batch_size = 4, epochs = 1000, loss_function = "mse")

    network.save_model("./model.json")

    network = Sequential.load_model("./model.json")

    print(np.argmax(network.forward(np.array(test_input)), axis = -1))