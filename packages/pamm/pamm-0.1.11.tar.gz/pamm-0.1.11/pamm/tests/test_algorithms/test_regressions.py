from pamm.algorithms.regression import(RegressionAlgorithm,
  TwoStageLeastSquaresAlgorithm,
  JackKnifeRegressionAlgorithm,
  IterationRegressionAlgorithm,
  RidgeRegressionAlgorithm,
  LassoRegressionAlgorithm,
  ElasticNetRegressionAlgorithm,
  WeigthedRegressionAlgorithm,
  WeightedTwoStageLeastSquaresAlgorithm,
  ModifyRegressionAlgorithm,
  QPRegressionAlgorithm,
  BatchGradientRegressionAlgorithm,
  StachosticGradientRegressionAlgorithm)


class TestBaseMethods:
    
    def test_predict(self, get_data):
        model = RegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.predict(get_data['x']).any() > 0
        
        
    def test_set_beta(self):
        model = RegressionAlgorithm(fit_bias = True)
        model.beta = (1,2,3,4)
        assert model.beta.shape == (4,1)
        
        
    def test_bias(self):
        model = RegressionAlgorithm(fit_bias=True)
        model.bias = 1
        assert model.bias == 1
        
        
    def test_fit_bias_true(self, get_data):
        model = RegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.bias != 0
        
        
    def test_fit_bias_false(self, get_data):
        model = RegressionAlgorithm(fit_bias = False)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.bias == 0
            
class TestNoParametrizeAlgorithm:
    
    def test_regression_algorithm(self, get_data):
        model = RegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_tsls_algoritm(self, get_data):
        model = TwoStageLeastSquaresAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], z = get_data['z'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_jackknife_algoritm(self, get_data):
        model = JackKnifeRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
     
         
    def test_iterations_algoritm(self, get_data):
        model = IterationRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
class TestRegularizationAlgorithm:

    def test_ridge_algorithm(self, get_data):
        model = RidgeRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_lasso_algorithm(self, get_data):
        model = LassoRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_elastic_net_algorithm(self, get_data):
        model = ElasticNetRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
class TestWeightedAlgorithm:
    
    def test_wls_algorithm(self, get_data):
        model = WeigthedRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], w=get_data['w'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_wtsls_algorithm(self, get_data):
        model = WeightedTwoStageLeastSquaresAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], z = get_data['z'], w=get_data['w'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
    
    
    def test_modify_algorithm(self, get_data):
        model = ModifyRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], q = get_data['q'], b_apr=get_data['beta_apr'], w=get_data['w'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
        
    def test_quad_prog_algorithm(self, get_data):
        model = QPRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], beta_min = get_data['beta_min'], beta_max = get_data['beta_max'], r=get_data['w'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
    
class TestGradientDeskAlgorithm:
    
    def test_batch_gradient_algorithm(self, get_data):
        model = BatchGradientRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
        
    
    def test_stachostic_gradient_algorithm(self, get_data):
        model = StachosticGradientRegressionAlgorithm(fit_bias = True)
        model.fit(x = get_data['x'], y = get_data['y'])
        assert model.beta.shape == get_data['beta'].shape
    