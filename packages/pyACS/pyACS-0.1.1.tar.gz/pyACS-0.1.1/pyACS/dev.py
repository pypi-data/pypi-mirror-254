import numpy as np
import pandas as pd
import timeit
from time import sleep

def test_list(n, m):
    c = list()
    a = list()
    for i in range(n):
        c.append(np.random.random(m))
        a.append(np.random.random(m))

def test_list_alloc(n, m):
    c = [None] * n
    a = [None] * n
    for i in range(n):
        c.append(np.random.random(m))
        a.append(np.random.random(m))

def test_numpy_array(n, m):
    c = np.empty([n, m])
    a = np.empty([n, m])

    for i in range(n):
        c[i, :] = np.random.random(m)
        a[i, :] = np.random.random(m)

def test_pandas_data_frame(n, m):
    d = pd.DataFrame(index=range(n), columns=['C%d' % x for x in range(m)] + ['A%d' % x for x in range(m)])
    for i in range(n):
        d.iloc[i, 0:m] = np.random.random(m)
        d.iloc[i, m:] = np.random.random(m)


def test_pandas_iloc(n):
    d = pd.DataFrame(index=range(n), columns=['A', 'B', 'C'])
    for i in range(n):
        d.iloc[i, 0] = int(np.random.random(1))


def test_pandas_loc(n):
    d = pd.DataFrame(index=range(n), columns=['A', 'B', 'C'])
    for i in range(n):
        d.loc[i, 0] = int(np.random.random(1))


def test_pandas_direct(n):
    d = pd.DataFrame(index=range(n), columns=['A', 'B', 'C'])
    for i in range(n):
        d.A[i] = int(np.random.random(1))


if __name__ == '__main__':
    print('list: %.3f s' % min(timeit.repeat(setup='from __main__ import test_list',
                            stmt='test_list(15000,75)',
                            repeat=3, number=10)))
    sleep(1)
    print('list: %.3f s' % min(timeit.repeat(setup='from __main__ import test_list_alloc',
                            stmt='test_list_alloc(15000,75)',
                            repeat=3, number=10)))
    sleep(1)
    print('numpy: %.3f s' % min(timeit.repeat(setup='from __main__ import test_numpy_array',
                            stmt='test_numpy_array(15000,75)',
                            repeat=3, number=10)))
    # sleep(1)
    # print('pandas: %.3f s' % min(timeit.repeat(setup='from __main__ import test_pandas_data_frame',
    #                         stmt='test_pandas_data_frame(15000,75)',
    #                         repeat=3, number=10))) # > 30 seconds

    # sleep(1)
    # print('iloc: %.3f s' % min(timeit.repeat(setup='from __main__ import test_pandas_iloc',
    #                                            stmt='test_pandas_iloc(15000)',
    #                                            repeat=3, number=10)))  # > 14 seconds
    # sleep(1)
    # print('loc: %.3f s' % min(timeit.repeat(setup='from __main__ import test_pandas_loc',
    #                                            stmt='test_pandas_loc(15000)',
    #                                            repeat=3, number=10)))  # > 34 seconds (computer regulated freq due to temp)
    # sleep(1)
    # print('direct: %.3f s' % min(timeit.repeat(setup='from __main__ import test_pandas_direct',
    #                                            stmt='test_pandas_direct(15000)',
    #                                            repeat=3, number=10)))  # > 39 seconds (computer regulated freq due to temp)