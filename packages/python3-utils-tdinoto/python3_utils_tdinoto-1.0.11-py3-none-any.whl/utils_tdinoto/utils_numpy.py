import numpy as np
from typing import Any


def find_most_frequent_value(input_array: np.ndarray) -> Any:
    """This function finds the most common value in the input numpy array
    Args:
        input_array: input array for which we want to find the most frequent value
    Returns:
        most_frequent_value: most frequent value
    """
    values, counts = np.unique(input_array, return_counts=True)

    idx = np.argmax(counts)
    most_frequent_value = values[idx]  # extract the most frequent element

    return most_frequent_value


def has_nans(input_array: np.ndarray) -> bool:
    """This function checks whether the input array contains any nan.
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array: input array where we check for nans
    Returns:
        array_has_nan: True if input_array contains nans; False otherwise
    """
    array_sum = np.sum(input_array)
    array_has_nan = np.isnan(array_sum)

    return array_has_nan


def is_binary(input_array: np.ndarray) -> bool:
    """This function checks whether the input array is binary (i.e. contains only 0s and 1s).
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array: input array that we want to inspect
    Returns:
        array_is_binary: True if input_array is binary; False otherwise
    """
    array_is_binary = np.array_equal(input_array, input_array.astype(bool))

    return array_is_binary


def has_values_all_in_range(input_array: np.ndarray,
                            low: int,
                            high: int) -> bool:
    """This function checks whether the input array has values that lie within the range (low, high).
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array: input array that we want to inspect
        low: lower bound
        high: upper bound
    Returns:
        array_is_withing_range: True if input_array has values in range (low, high); False otherwise
    """
    mask_array_bool = (input_array > low) & (input_array < high)

    if False in mask_array_bool:  # if there is just one False value
        array_is_withing_range = False
    else:  # if instead all values are True
        array_is_withing_range = True

    return array_is_withing_range


def pad_image_to_specified_shape(input_img: np.ndarray,
                                 desired_x_dim: int,
                                 desired_y_dim: int) -> np.ndarray:
    """This function zero-pads input_img up to the specified shape (desired_x_dim, desired_y_dim)
    Args:
        input_img: input image that we want to pad
        desired_x_dim: desired dimension 1
        desired_y_dim: desired dimension 2
    Returns:
        padded_img: output padded image
    """

    assert len(input_img.shape) == 2, "This function is intended for 2D arrays"

    # extract dims of input image
    h = input_img.shape[0]
    w = input_img.shape[1]

    # extract padding width (before and after) for rows
    a = (desired_x_dim - h) // 2
    aa = desired_x_dim - a - h

    # extract padding width (before and after) for cols
    b = (desired_y_dim - w) // 2
    bb = desired_y_dim - b - w

    padded_img = np.pad(input_img, pad_width=((a, aa), (b, bb)), mode='constant', constant_values=0)

    return padded_img


def generate_binary_array_with_exact_proportion(array_len: int,
                                                nb_zeros: int,
                                                shuffle: bool = True) -> np.ndarray:
    """This function creates a 1D binary array with an exact proportion of 0s and 1s.
    The array will contain exactly nb_zeros 0s, and (array_len - nb_zeros) 1s. By
    default, the generated array is shuffled.
    Args:
        array_len: length of generated array
        nb_zeros: number of 0s in the generated array (the rest will be 1s)
        shuffle: whether to shuffle the generated array
    Returns:
        generated_binary_array: generated binary array
    """
    generated_binary_array = np.array([0] * nb_zeros + [1] * (array_len - nb_zeros))
    if shuffle:
        np.random.shuffle(generated_binary_array)

    return generated_binary_array


def mean_excluding_zeros(input_array: np.ndarray) -> float:
    """This function computes the mean of non-zero values
    Args:
        input_array: input array for which we want to compute the mean
    Returns:
        mean_value_excluding_zeros: the arithmetic mean computed neglecting all zero elements
    """
    input_array = input_array.astype('float')  # cast array to float
    input_array[input_array == 0] = np.nan  # set zero values to NaN
    mean_value_excluding_zeros = np.nanmean(input_array)

    return mean_value_excluding_zeros


def is_empty(input_array: np.ndarray) -> bool:
    """This function checks whether the input array is empty.
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array: input array that we want to inspect
    Returns:
        array_is_empty: True if input_array is empty; False otherwise
    """
    array_is_empty = input_array.size == 0

    return array_is_empty


def binarize_array(input_array: np.ndarray,
                   threshold: float = 0.5) -> np.ndarray:
    """This function binarizes the input array by converting values to either 0 or 1 based on the threshold.
    Args:
        input_array (numpy.ndarray or list): The input array to be binarized.
        threshold: The threshold value to use for binarization. Default is 0.5.
    Returns:
        binarized_array: The binarized array.
    """
    # Apply binarization using element-wise comparison
    binarized_array = (input_array >= threshold).astype(int)

    return binarized_array


def arrays_are_identical(arr_np1: np.ndarray,
                         arr_np2: np.ndarray) -> bool:
    """Check whether two NumPy arrays are exactly identical.
    Args:
        arr_np1: The first NumPy array.
        arr_np2: The second NumPy array.
    Returns:
        are_identical: True if the two arrays are identical, False otherwise.
    """
    # Check if shapes are equal
    if arr_np1.shape != arr_np2.shape:
        raise ValueError(f"Shapes are different. arr_np1.shape = {arr_np1.shape}, arr_np2.shape = {arr_np2.shape}")

    # Check if elements are equal
    are_identical = np.array_equal(arr_np1, arr_np2)

    return are_identical
