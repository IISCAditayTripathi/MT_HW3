import numpy
import math

import argparse

parser = argparse.ArgumentParser(description='This script performs GSM orthogalization')

parser.add_argument('--mode', type=str, default='classical', help='Classical/Modified (default: classical)')

args = parser.parse_args()


v1 = numpy.array([1, -1, 3])
v2 = numpy.array([3, 2, 5])
v3 = numpy.array([3, 1, 4])
if (args.mode == 'classical'):
    u1 = v1/numpy.linalg.norm(v1, ord=2)
    u2_dash = v2 - numpy.dot(v2,u1)*u1
    u2 = u2_dash/numpy.linalg.norm(u2_dash, ord=2)
    u3_dash = v3 - numpy.dot(v3,u1)*u1 - numpy.dot(v3, u2)*u2
    u3 = u3_dash/numpy.linalg.norm(u3_dash, ord=2)

    print('u1: [%f %f %f]' % (u1[0], u1[1], u1[2]))
    print('u2: [%f %f %f]' % (u2[0], u2[1], u2[2]))
    print('u3: [%f %f %f]' % (u3[0], u3[1], u3[2]))