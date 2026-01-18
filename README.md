# Adaptive Goodness-of-Fit Testing for Exponential Hawkes Processes

This repository implements the statistical framework described in the research project "Adaptive Goodness-of-Fit Testing for Exponential Hawkes Process" (January 2026). The project focuses on developing a robust testing procedure to verify if observed point processes follow an exponential Hawkes model.

## Code Structure & File Descriptions

### 1. `Thinning.py`
This file contains the `thinning_hawkes` class, which implements **Ogata's Thinning Algorithm** to simulate different kernels (`exponential`, `gaussian`, `box_periodic`, `inhibitory_exponential`, etc.).

### 2. `hawkes_inference.py`
- **`estimate_hawkes_params_`**: Implements the Maximum Likelihood Estimator (MLE) for the exponential kernel by aggregating n processes.
- **`compensator_expo_at_times_split`**: Calculates the compensator function, a crucial step for the time-change transformation.
- **`build_cumulation`**: Merges p(n) transformed processes into a single unified timeline to form the cumulative process.

### 3. `hawkes_statistical_tests.py`
Implements the core testing logic and Monte Carlo simulations.
- **`collect_ks_stats`**: Performs M simulations to compute the Z statistic and track the rejection rate.
- **`run_and_save_experiment`**: Automates sensitivity analysis by varying specific parameters and plotting the rejection proportion.

### 4. `main.py`
The execution script that connects all modules.