import numpy as np
from typing import Optional, Union

def count_nonzero_elements(arr: np.array, tolerance: Optional[float] = 1e-15, axis = None) -> Union[int, np.ndarray]:
    """
    Count the number of non-zero elements in an array.

    Parameters
    ----------
    arr : numpy.array
        The input array of any dimension (1D, 2D, or 3D).
    tolerance : float, optional
        The tolerance for considering floating-point values greater than 0.
    axis : int or Tuple[int], optional
        Axis or axes along which to count non-zero elements. Default is None.

    Returns
    -------
    Union[int, np.ndarray]: Returns either an integer (for None), or an array based on the 'axis'.
      - For None: Total Non-Zero Elements in Array.
      - For axis: Non-Zero Elements along the specified axis/axes.

    Raises
    ------
    TypeError
        If the input is not a numpy array, or the input array does not contain numeric data types.

    Examples
    --------
    >>> import numpy as np
    >>> from mds_array_manipulation import mds_array_manipulation as am
    >>> arr = np.array([0, 1, 2])
    >>> am.count_nonzero_elements(arr)
    2
    >>> arr2d = np.array([[0, 1, 2], [3, 0, 5], [0, 7, 8]])
    >>> am.count_nonzero_elements(arr2d, axis=1)
    array([2, 2, 2])
    >>> am.count_nonzero_elements(arr2d, axis=0)
    array([1, 2, 3])
    """

    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if np.issubdtype(arr.dtype, np.number) == False:
        raise TypeError("Input array must be numeric data only")

    arr = arr.astype(float)

    if axis is None:
        return np.sum(np.abs(arr) > tolerance)
    else:
        return np.sum(np.abs(arr) > tolerance, axis=axis)
