# Packages from requirements.
from numpy import ndarray, sum as numpy_sum


def mse(calc: ndarray, true: ndarray) -> ndarray:
    """
    Calculate the mean squared error per output from the given arrays.

    Parameters
    ----------
    calc: ndarray
        Vector containing all the calculated or predicted values.
    true: ndarray
        Vector containing all the true or expected values.

    Returns
    -------
    ndarray [1 x m]:
        Mean squared error per output.
    """
    squared_error = (true - calc) ** 2
    return numpy_sum(squared_error / len(squared_error), axis=0)


def mse_prime(calc: ndarray, true: ndarray) -> ndarray:
    """
    Calculate the mean squared error derivative from the given arrays.

    Parameters
    ----------
    calc: ndarray [n x m]
        Array containing all the calculated or predicted values.
    true: ndarray [n x m]
        Array containing all the true or expected values.

    Returns
    -------
    ndarray [n x m]:
        Mean squared error derivative array.
    """
    return -2 * (true - calc)
