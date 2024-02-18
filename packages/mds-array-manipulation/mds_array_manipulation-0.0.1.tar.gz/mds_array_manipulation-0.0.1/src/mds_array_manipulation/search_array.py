import numpy as np 

def search_array(arr, elem):
    """
    Search for elem in a numpy array.
    
    Parameters
    ----------
    arr : numpy.array
        The numpy array to search
    elem : numeric or string
        Object to search for in the array
    
    Returns
    -------
    int
        Index of the first occurence of the element in the array, -1 if not found

    Raises
    ------
    TypeError
        If the input is not a numpy array, or does not contain numeric or string values.
    ValueError
        If the input array is not 1-dimensional.

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation.mds_array_manipulation import search_array
    >>> arr = np.array([20, 10, 20, 30, 50, 90, 60])
    >>> search_array(arr, 50)
    4
    >>> search_array(arr, 100)
    -1
    >>> search_array(arr, 20)
    0
    """

    #Only accept numpy arrays
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input array must be numpy array")
    
    #Only accept numeric or string arrays
    if not (np.issubdtype(arr.dtype, np.number) or arr.dtype.kind in {'U', 'S'}):
        raise TypeError("Input array must be numeric or string array")
    
    #Only accept 1D array
    if len(arr.shape) > 1:
        raise ValueError("Input array must be 1D array")

    i = 0 
    while i < len(arr):
        if arr[i] == elem:
            return i
        i += 1
    return -1