from pamm.metricks import numeric as nm


class TestNumericMetrick:
    
    def test_mse(self, get_vectors):
        solution = nm.mse(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution == (get_vectors['shift']**2)
        
        
    def test_rmse(self, get_vectors):
        solution = nm.rmse(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution == get_vectors['shift']
        
        
    def test_mae(self, get_vectors):
        solution = nm.mae(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution == get_vectors['shift']
        
    
    def test_mspe(self, get_vectors):
        solution = nm.mspe(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution > get_vectors['shift']
        
    
    def test_mape(self, get_vectors):
        solution = nm.mape(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution > get_vectors['shift']
        
        
    def test_smape(self, get_vectors):
        solution = nm.smape(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution > get_vectors['shift']
        
        
    def test_mre(self, get_vectors):
        solution = nm.mre(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution > get_vectors['shift']
        
        
    def test_rmsle(self, get_vectors):
        solution = nm.rmsle(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution < get_vectors['shift']
        
        
    def test_corr(self, get_vectors):
        solution = nm.corr(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution > .98
        
        
    def test_r2(self, get_vectors):
        solution = nm.r2(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'])
        assert solution < get_vectors['shift']
        
        
    def test_adjusted_r2(self, get_vectors):
        solution = nm.adjusted_r2(major_ts = get_vectors['major_ts'], minor_ts = get_vectors['minor_ts'], count_features= get_vectors['shift'])
        assert solution < get_vectors['shift']