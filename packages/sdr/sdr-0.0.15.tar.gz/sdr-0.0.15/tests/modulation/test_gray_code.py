import numpy as np
import pytest

import sdr


def test_exceptions():
    with pytest.raises(ValueError):
        # n must be at least 1
        sdr.binary_code(0)


def test_1():
    code = sdr.gray_code(1)
    code_truth = [0, 1]
    assert isinstance(code, np.ndarray)
    assert np.array_equal(code, code_truth)


def test_2():
    code = sdr.gray_code(2)
    code_truth = [0, 1, 3, 2]
    assert isinstance(code, np.ndarray)
    assert np.array_equal(code, code_truth)


def test_3():
    code = sdr.gray_code(3)
    code_truth = [0, 1, 3, 2, 6, 7, 5, 4]
    assert isinstance(code, np.ndarray)
    assert np.array_equal(code, code_truth)


def test_4():
    code = sdr.gray_code(4)
    code_truth = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
    assert isinstance(code, np.ndarray)
    assert np.array_equal(code, code_truth)
