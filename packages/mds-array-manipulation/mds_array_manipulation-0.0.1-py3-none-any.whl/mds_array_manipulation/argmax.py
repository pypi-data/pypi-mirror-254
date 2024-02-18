import numpy as np

def argmax(arr, axis=None):
    """
    Returns the indices of the maximum values along an axis from given array.

    Parameters
    ----------
    arr : numpy.array
        Input array.
    axis : int, optional
        Axis along which to operate. By default, flattened input is used.

    Returns
    -------
    indices : int or tuple of ints
        Indices of the maximum values along the specified axis.

    Raises
    ------
    TypeError
        If the input is not a numpy array.
    ValueError
        If the input array is empty, or the axis specified is greater than the number of dimensions

    Notes
    -----
    If there are multiple occurrences of the maximum values, the indices
    corresponding to the first occurrence are returned.

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation.mds_array_manipulation import argmax
    >>> a = np.arange(6).reshape(2,3)
    >>> a
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> argmax(a)
    5
    >>> argmax(a, axis=0)
    array([1, 1, 1])
    >>> argmax(a, axis=1)
    array([2, 2])

    >>> b = np.arange(6)
    >>> b[1] = 5
    >>> b
    array([0, 5, 2, 3, 4, 5])
    >>> argmax(b)  # Only the first occurrence is returned.
    1
    """
    # Coding Part
    # Check numpy array, not empty numpy array, and not specified axis=1 when input array is 1D numpy array
    if not isinstance(arr, np.ndarray):
	    raise TypeError("Input array is not a numpy array. Please enter only numpy array.")
    if arr.size == 0: 
	    raise ValueError("Input array is an empty array. Please do not enter an empty array.")
    if (arr.ndim == 1) and (axis == 1): 
	    raise ValueError("Cannot enter a 1D numpy array with axis = 1. Please enter again.")

    # Case of no axis is specified
    if axis is None:
        # Flatten the array if no axis is specified
        flattened_array = arr.flatten()
        max_value = None
        max_index = None
        for i, value in enumerate(flattened_array):
            if max_value is None or value > max_value:
                max_value = value
                max_index = i
        return max_index

    # Case of axis is specified
    elif (axis == 0) or (axis == 1):
        # Find the maximum along the specified axis
        max_values = [None] * arr.shape[axis]
        max_indices = [None] * arr.shape[axis]
        if axis == 0:
            for i in range(arr.shape[axis]):
                for j in range(arr.shape[1]):
                    if max_values[i] is None or arr[i, j] > max_values[i]:
                        max_values[i] = arr[i, j]
                        max_indices[i] = j
        elif axis == 1:
            for j in range(arr.shape[axis]):
                for i in range(arr.shape[0]):
                    if max_values[j] is None or arr[i, j] > max_values[j]:
                        max_values[j] = arr[i, j]
                        max_indices[j] = i
        return max_indices
    else:
	    raise ValueError("Error caused by axis specified other than 0 or 1.")
