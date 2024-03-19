import numpy

bits = "1011111010101100010011101100110001101110110011000100111011111010011101101000110011111010010011101100110000101110001011101100110001000110111110101010110010010110111110100010110001001110010001101100110011100110100011001000001011011110100100101010001011001010"

# Passamos a os bits para uma matriz
int_bits = [int(bit) for bit in bits]
matrix = numpy.array(int_bits).reshape(16, 16)

# Invertemos a matriz
reversed_matrix = numpy.flip(matrix)

# Retornamos os bits da matriz como uma string
reversed_bit_string = ''.join([str(int(bit)) for bit in reversed_matrix.flatten()])
print(reversed_bit_string)