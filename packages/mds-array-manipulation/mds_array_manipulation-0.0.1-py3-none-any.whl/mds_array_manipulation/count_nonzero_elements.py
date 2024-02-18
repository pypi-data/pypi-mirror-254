
import numpy as np
def count_nonzero_elements(arr,tolerance=1e-15):
    """
    Count the number of non zero elements in an array.
    
    Parameters
    ----------
    arr : numpy.array
        The Input array of any dimension (1D, 2D or 3D)
    tolerance : float, optional
        The tolerance for considering floating point values greater than 0
        
    Returns
    -------
    dict : A dictionary containing information about non-zero elements. Below are the keys in the dictionary
      - For 1D array: {'Total Non-Zero Elements in Array': total_nonzero}
      - For 2D or 3D array:
        {
          'Non-Zero Elements in Rows': row_counts,
          'Non-Zero Elements in Columns': col_counts,
          'Total Non-Zero Elements in Array': total_nonzero
        }

    Raises
    ------
    TypeError
        If the input is not a numpy array, or the input array does not contain numeric data types

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation import mds_array_manipulation as am
    >>> arr = np.array([0, 1, 2])
    >>> am.count_nonzero_elements(arr)
    {'Total Non-Zero Elements in Array': 2}
    >>> arr2d = np.array([[0, 1, 2], [3, 0, 5], [0, 7, 8]])
    >>> am.count_nonzero_elements(arr2d)
        {'Total Non-Zero Elements in Array': 6, 'Non-Zero Elements in Rows': array([2, 2, 2]), 'Non-Zero Elements in Columns': array([1, 2, 3])}
    """
    
    
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if np.issubdtype(arr.dtype, np.number) == False:
        raise TypeError("Input array must contain numeric data types only")
    
    arr = arr.astype(float)
    result = {}
    total_nonzero = np.sum(np.abs(arr) > tolerance)

    if arr.ndim == 1:
        result["Total Non-Zero Elements in Array"] = total_nonzero
    elif arr.ndim == 2:
        row_counts = np.sum(np.abs(arr) > tolerance, axis=1, keepdims=True)
        col_counts = np.sum(np.abs(arr) > tolerance, axis=0, keepdims=True)
        result["Total Non-Zero Elements in Array"] = total_nonzero
        result["Non-Zero Elements in Rows"] = row_counts.reshape(-1)
        result["Non-Zero Elements in Columns"] = col_counts.reshape(-1)
       
    elif arr.ndim >= 3:
        row_counts = np.sum(np.abs(arr) > tolerance, axis=2, keepdims=True)
        col_counts = np.sum(np.abs(arr) > tolerance, axis=1, keepdims=True)
        result["Total Non-Zero Elements in Array"] = total_nonzero
        result["Non-Zero Elements in Rows"] = row_counts.reshape(-1)
        result["Non-Zero Elements in Columns"] = col_counts.reshape(-1)

    return result