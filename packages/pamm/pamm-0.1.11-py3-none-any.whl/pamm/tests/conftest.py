"""Conftest for genering test-data"""

import pytest
import random
import numpy as np


@pytest.fixture(scope='module')
def get_ts():
    size_major, size_minor = random.randint(1,437), random.randint(1000-7,27182)
    major_ts = np.random.rand(size_major, 2)
    minor_ts = np.random.rand(size_minor, 2)
    
    return {'major_ts': major_ts, 'minor_ts': minor_ts}


@pytest.fixture(scope='module')
def get_vectors():
    num = random.randint(1,437)
    shift = random.randint(3,22)
    major_ts = np.random.rand(num, 1)
    minor_ts = shift + major_ts
    return {'major_ts': major_ts, 'minor_ts': minor_ts, 'shift': shift}


@pytest.fixture(scope = "module")
def get_data(count_beta: int =  5):
    beta = np.random.rand(count_beta, 1)
    x = np.random.rand(count_beta * 20, count_beta)
    z = np.random.rand(count_beta * 20, count_beta + 2)
    w = np.eye(count_beta * 20)
    beta_apr = np.ones(count_beta).reshape((count_beta,1))
    q = np.eye(count_beta)
    beta_min = np.ones(count_beta).reshape((count_beta,1)) * -1
    beta_min[0,0] = 0.0000000009
    beta_max = np.ones(count_beta).reshape((count_beta,1)) * 5
    beta_max[0,0] = 0.09
    y = x @ beta
    return {'x': x, 'z': z, 'w': w, 'y': y, 'q': q, 'beta_apr': beta_apr, 'beta': beta, 'beta_max': beta_max, 'beta_min': beta_min}