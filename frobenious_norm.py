import numpy
import math

n_rows = 10
n_columns = 10

A = numpy.random.rand(n_rows, n_columns)

A_trans = numpy.transpose(A)

B = numpy.dot(A_trans, A)

i = B.shape[0]

t = 0
for j in range(i):
    t = t + B[j][j]

print(math.sqrt(t))