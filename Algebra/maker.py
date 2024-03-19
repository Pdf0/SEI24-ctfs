import numpy

flag = "SEI{A1g3br4_i5_b3tt3r_1n_r3v3r5}"

# Passamos a flag para binário
binary_flag = [int(bit) for bit in ''.join(format(ord(char), '08b') for char in flag)]

# Criamos uma matriz quadrada já que ficamos com 256 bits (16*16)
matrix = numpy.array(binary_flag).reshape(16, 16)

# Invertemos a matriz
reversed_matrix = numpy.flip(matrix)

# Retornamos os bits da matriz como uma string
reversed_bit_string = ''.join([str(int(bit)) for bit in reversed_matrix.flatten()])
print(reversed_bit_string)