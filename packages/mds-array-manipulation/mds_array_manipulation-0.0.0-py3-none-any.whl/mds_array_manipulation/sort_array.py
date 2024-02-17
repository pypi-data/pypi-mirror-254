import numpy as np

def sort_array(arr):
    """
    Sort a numpy array in ascending or alphabetical order.
    The sorting is case-insensitive for strings.

    Parameters
    ----------
    arr : numpy.array
        The numpy array to be sorted. The array can contain numerical 
        or string values.

    Returns
    -------
    numpy.array
        A new numpy array sorted in ascending or alphabetical order.

    Raises
    ------
    TypeError
        If the input is not a numpy array.
    ValueError
        If the input array is not 1-dimensional.

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation import mds_array_manipulation as am
    >>> arr = np.array([20, 10, 40, 30, 50, 90, 60])
    >>> sort_array(arr)
    array([10, 20, 30, 40, 50, 60, 90])

    >>> arr_str = np.array(["orange", "grape", "apple"])
    >>> sort_array(arr_str)
    array(['apple', 'grape', 'orange'])
    """
    # Check if input is a numpy array
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")

    # Check if the array is 1D
    if arr.ndim != 1:
        raise ValueError("Input array must be 1D")

    # Handle case of empty array or array with single element
    if arr.size <= 1:
        return arr
    
    # Perform insertion sort
    arr_list = arr.tolist()

    for i in range(1, len(arr_list)):
        key = arr_list[i]
        j = i - 1

        while j >= 0 and ((str(arr_list[j]).lower() > str(key).lower()) if isinstance(key, str) else (arr_list[j] > key)):
            arr_list[j + 1] = arr_list[j]
            j -= 1

        arr_list[j + 1] = key

    return np.array(arr_list)