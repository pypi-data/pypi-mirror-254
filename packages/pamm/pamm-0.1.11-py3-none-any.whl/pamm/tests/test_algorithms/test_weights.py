from pamm.algorithms.weighing.weights_data_algorithms import inversely, equal, time_booster
from pamm.algorithms.weighing.weigts_beta_algorithms import max_truth


import random

class TestBetaWeights:
    
    def test_max_truth(self, get_data):
        res = max_truth(get_data['beta'])
        assert get_data['beta'].shape[0] == res.shape[random.randint(0,1)]

class TestDataWeights:
    
    def test_inversely(self, get_ts):
        res = inversely(get_ts['minor_ts'])
        assert get_ts['minor_ts'].shape[0] == res.shape[random.randint(0,1)]
        
    
    def test_equal(self, get_ts):
        res = equal(get_ts['minor_ts'])
        size = get_ts['minor_ts'].shape[0]
        rnd_number = random.randint(0,size)
        assert size == res.shape[random.randint(0,1)]
        assert res[rnd_number,rnd_number] == 1
        
    
    def test_time_booster(self, get_ts):
        res = time_booster(get_ts['minor_ts'])
        assert get_ts['minor_ts'].shape[0] == res.shape[random.randint(0,1)]
          