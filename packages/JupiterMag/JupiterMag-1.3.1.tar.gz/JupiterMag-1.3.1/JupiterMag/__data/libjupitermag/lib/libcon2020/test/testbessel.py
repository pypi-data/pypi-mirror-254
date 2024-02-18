import numpy as np
from scipy.special import j0,j1
import time

def TestBessel():
	n = 100000
	x0 = np.random.rand(n)*5
	x1 = np.random.rand(n)*5 + 5

	dt = np.zeros(5,dtype='float64')

	for i in range(0,5):
		t0 = time.time()
		j = j0(x0)
		t1 = time.time()
		dt[i] = t1 - t0

	print("j0 (0-5): {:f} +/- {:f}".format(np.mean(dt),np.std(dt)))

	for i in range(0,5):
		t0 = time.time()
		j = j0(x1)
		t1 = time.time()
		dt[i] = t1 - t0

	print("j0 (5-10): {:f} +/- {:f}".format(np.mean(dt),np.std(dt)))

	for i in range(0,5):
		t0 = time.time()
		j = j1(x0)
		t1 = time.time()
		dt[i] = t1 - t0

	print("j1 (0-5): {:f} +/- {:f}".format(np.mean(dt),np.std(dt)))

	for i in range(0,5):
		t0 = time.time()
		j = j1(x1)
		t1 = time.time()
		dt[i] = t1 - t0

	print("j1 (5-10): {:f} +/- {:f}".format(np.mean(dt),np.std(dt)))

if __name__ == '__main__':
	TestBessel()