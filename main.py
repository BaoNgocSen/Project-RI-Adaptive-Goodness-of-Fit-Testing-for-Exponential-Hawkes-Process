import numpy as np
from hawkes_statistical_tests import run_and_save_experiment

M = 300
n = 3000
p = int((n)**(2/3))
T = 20

# Baseline parameters
base_params = {'mu': 0.2, 'alpha': 0.5, 'beta': 1, 'peri': 2, 'epsilon': 0.3}
kernels = ['box_periodic']

mu_range = [0.2, 0.4, 0.8, 1]
beta_range = [0.6, 0.8, 1, 1.5, 1.8]
peri_range = [0.5, 1, 1.5, 2.0 ,5.0 ]
epsilon_range = [0.1, 0.2, 0.3, 0.5, 0.8] 
# 1. Varying Beta
run_and_save_experiment('beta', beta_range, base_params, kernels, M, p, n, T)

# 2. Varying Mu 
run_and_save_experiment('mu', mu_range, base_params, kernels, M, p, n, T)

# 3. Varying Periodic (peri)S
run_and_save_experiment('peri', peri_range, base_params, kernels, M, p, n, T)

run_and_save_experiment('epsilon', epsilon_range, base_params, kernels, M, p, n, T)