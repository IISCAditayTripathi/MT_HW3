import numpy

import argparse
import math

def GSM(A):
    dim = numpy.size(A, 1)

    x = {}
    u = {}

    for i in range(dim):
        x[str(i+1)] = A[:,i]

    for k in range(dim):
        if (k == 0):
            # print (k)
            u[str(k + 1)] = x[str(k + 1)] / numpy.linalg.norm(x[str(k + 1)], ord=2)
            print 'u' + str(k + 1) + ':',
            print(u[str(k + 1)])
            for i in range(dim - k - 1):
                u[str(i + 1 + k + 1)] = x[str(i + 1 + k + 1)]
                # print(u[str(i+1+k+1)])

        else:
            for i in range(dim - k):
                # print(max(0, i-1))
                # print(k)
                u[str(i + 1 + k)] = u[str(i + 1 + k)] - numpy.dot(numpy.transpose(u[str(max(0, i - 1) + k)]),
                                                                  u[str(i + k + 1)]) * u[str(max(0, i - 1) + k)]
            u[str(k + 1)] = u[str(k + 1)] / numpy.linalg.norm(u[(str(k + 1))], ord=2)
            print 'u' + str(k + 1) + ':',
            print(u[str(k + 1)])
    B = u['1']
    # print(B)
    for i in range(dim-1):
        B = numpy.vstack((B, u[str(i+2)]))
    return B

def QR_factors(A):
    U = GSM(A)
    R = numpy.dot(U,A)

    Q = numpy.transpose(U)
    return Q, R


X = numpy.array([[1,-1,3], [3,2,5], [3,1,4],])


Q,R = QR_factors(X.transpose())

print(R)
# print(GSM(X.transpose()))


