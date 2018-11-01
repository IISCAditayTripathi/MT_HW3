import numpy
import math
import argparse

parser = argparse.ArgumentParser(description='Script to calculate Frobenious Norm of a random matrix')

parser.add_argument('--row_dim', type=int, default=10, help='Matrix row dimension (default:10)')

parser.add_argument('--col_dim', type=int, default=20, help='Matrix column dimension (default:20)')


args = parser.parse_args()

n_rows = args.row_dim
n_columns = args.col_dim

A = numpy.random.rand(n_rows, n_columns)

A_trans = numpy.transpose(A)

B = numpy.dot(A_trans, A) # (A_trans*A)

i = B.shape[0]            # Matrix dimension

t = 0
for j in range(i):
    t = t + B[j][j]

print('Frobenious Norm of Random matrix with dimension %dx%d is:%f'%(n_rows, n_columns, math.sqrt(t)))