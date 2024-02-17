# Packages from requirements.
from numpy import ndarray, exp


def sigmoid(x: ndarray) -> ndarray:
    """
    Calculate output "y" from input "x" based on the sigmoid function:

    y(x) = 1 / (1 + (e ** -x))

    Parameters
    ----------
    x: ndarray [n x m]
        Input for the sigmoid function.

    Returns
    -------
    ndarray [n x m]:
        Output from the sigmoid function.
    """
    return 1 / (1 + exp(-x))


def sigmoid_prime(x: ndarray) -> ndarray:
    """
    Calculate output "y_prime" from input "x" based on the sigmoid derivative:

    y(x) = 1 / (1 + (e ** -x))
    y_prime(x) = y(x) * (1 - y(x))

    Parameters
    ----------
    x: ndarray [n x m]
        Input for the sigmoid derivative.

    Returns
    -------
    ndarray [n x m]:
        Output from the sigmoid derivative.
    """
    y = sigmoid(x=x)
    return y * (1 - y)
