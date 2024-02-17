# SnoScience

A package optimised for building small neural networks.

![](..\data\epochs_200.jpg)

The MNIST dataset has been used for training. Each network is trained by using 64 samples from this dataset per epoch for 200 epochs.
As can be seen from the graph, use Tensorflow or equivalent for networks with more than 3 layers (n>3) and/or more than 20 neurons per layer.
SnScience networks with one (n=2) or no hidden layers (n=1) are extremely fast.

## Installation

To install the SnoScience package either:
- run the command 'pip install snoscience' in the command line.
- install the package via your IDE.

## Features

#### SnoScience.networks module

1. The user is able to create a neural network capable of being trained and making predictions:
   1. this network is able to process an arbitrary number of inputs.
   2. this network can consist of an arbitrary number of layers.
   3. each layer in this network can consist of an arbitrary number of neurons.
2. The neural network supports the following activation functions:
   1. sigmoid.
3. The neural network supports the following loss functions:
   1. mean squared error (MSE).
4. The neural network supports the following optimisers:
   1. stochastic gradient descent (SGD).
5. The user can train the neural network with a single command:
   1. all inputs are checked for validity before the training proceeds.
6. The user can let the network make predictions with a single command:
   1. all inputs are checked for validity before predictions are given.
   2. these predictions can be regressions of an arbitrary size.
   3. these predictions can be classifications of an arbitrary size.

#### SnoScience.metrics module

1. The user is able to calculate the mean squared error of a regression.
2. The user is able to calculate the accuracy of a classification.

## Usage

    from snoscience.networks import NeuralNetwork
    from snoscience.metrics import calculate_mse, calculate_accuracy

    # Create model.
    model = NeuralNetwork(inputs=9, loss="MSE", optimiser="SGD")
    model.add_layer(neurons=2, activation="sigmoid")
    model.add_layer(neurons=1, activation="sigmoid")

    # Define optimizer hyperparameters.
    rate = 0.01

    # Train model.
    model.train(x=x_train, y=y_train, epochs=1000, samples=32, rate=rate, log=False)

    # Make predictions (classification).
    y_calc = model.predict(x=x_test, classify=True)
    
    # Make predictions (regression).
    y_calc = model.predict(x=x_test, classify=False)

    # Calculate performance.
    mse = calculate_mse(calc=y_calc, true=y_test)
    accuracy = calculate_accuracy(calc=y_calc, true=y_test)

## Calculations

#### Total derivative for neuron

    dL / dy_1 = (dy_2_1 / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_1 / dy_1) * (dy_3_2 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_1 / dy_1) * (dy_3_P / dy_2) ... (dL / dy_M_1) +  
                ...  
                (dy_2_1 / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_1 / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_2) +  
                (dy_2_1 / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_N) +  
                ...  
                (dy_2_Q / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_Q / dy_1) * (dy_3_2 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_Q / dy_1) * (dy_3_P / dy_2) ... (dL / dy_M_1) +  
                ...  
                (dy_2_Q / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_1) +  
                (dy_2_Q / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_2) +  
                (dy_2_Q / dy_1) * (dy_3_1 / dy_2) ... (dL / dy_M_N) +  
                ...  
                (dy_2_Q / dy_1) * (dy_3_P / dy_2) ... (dL / dy_M_N)  

    L = loss
    y_X = neuron in layer X.
    
    M = last layer.
    N = last neuron in last layer.
    P = last neuron in third layer.
    Q = last neuron in second layer.
    
    Applicable chain rule:
    
    dy_A / dy_B = y_dot_A * w_A[position_B]

    A = current neuron
    B = neuron from previous layer
    
    Chain rule needs to be applied everywhere except for the starting neuron.

#### Total derivative for neuron weights and bias

    dL / db = sum(dL / dy_A)
    dL / dw = sum((dL / dy_A) * y_B)

    A = current neuron
    B = previous layer
    
    Example
    -------
    y_B = [[1, 2, 3],
           [4, 5, 6]]

    dL / dy_A = [[1],
                 [2]]
    
    dL / db = 3
    dL / dw = [[9],
               [12],
               [15]]

#### Stochastic gradient descent

    b_new = b_old - (learn * dL / db)
    w_new = w_old - (learn * dL / dw)
    
    Example
    -------
    rate = 0.1
    
    b_old = 1
    w_old = [[1],
             [1],
             [1]]
    
    dL / db = 3
    dL / dw = [[9],
               [12],
               [15]]
               
    b_new = 0.7
    w_new = [[0.1],
             [-0.2],
             [-0.5]]

## Changelog

#### v1.0.0

- SnoScience.networks features 1 through 6 added.
- SnoScience.metrics features 1 and 2 added.

#### v0.1.0

- Initial release.
