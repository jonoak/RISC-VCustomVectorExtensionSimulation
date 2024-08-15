import numpy as np
from main import RISCVCustomExtension


def test_vector_addition():
    vector_a = RISCVCustomExtension()
    vector_b = RISCVCustomExtension()
    vector_a.load_data([1, 2, 3, 4])
    vector_b.load_data([5, 6, 7, 8])
    result = vector_a.vector_add(vector_b)
    expected = np.array([6, 8, 10, 12])
    assert np.array_equal(result, expected), f'Expected {expected}, but got {result}'


def test_vector_addition_different_length():
    vector_a = RISCVCustomExtension()
    vector_b = RISCVCustomExtension()
    vector_a.load_data([1, 2, 3])  # Length is 3
    vector_b.load_data([5, 6, 7, 8])  # Length is 4
    try:
        vector_a.vector_add(vector_b)
    except ValueError as ve:
        assert str(ve) == 'Vectors must be of the same length.', f'Unexpected error message: {ve}'
    else:
        assert False, 'Expected ValueError was not raised.'


if __name__ == '__main__':
    test_vector_addition()
    test_vector_addition_different_length()
    print('All tests passed!')