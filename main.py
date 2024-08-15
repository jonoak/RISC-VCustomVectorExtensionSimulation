import numpy as np

class RISCVCustomExtension:
    def __init__(self):
        self.vector_register = np.zeros(4)

    def load_data(self, data):
        '''Load data into the vector register.'''
        self.vector_register = np.array(data)

    def vector_add(self, other):
        '''Perform vector addition with another vector register.'''
        if len(other.vector_register) != len(self.vector_register):
            raise ValueError('Vectors must be of the same length.')
        return self.vector_register + other.vector_register

    def __str__(self):
        return f'Vector Register: {self.vector_register}'

if __name__ == '__main__':
    vector_a = RISCVCustomExtension()
    vector_b = RISCVCustomExtension()
    vector_a.load_data([1, 2, 3, 4])
    vector_b.load_data([5, 6, 7, 8])
    result = vector_a.vector_add(vector_b)
    print('Result of Vector Addition:', result)