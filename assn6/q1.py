from scipy.optimize import minimize
import numpy as np

if __name__ == "__main__":
    func = lambda x: 5 * x[0] - 7 * x[1] + 2 * x[2] - x[3]
    cons = ({'type': 'ineq', 'fun': lambda x: -(8 * x[0] + x[1] - x[2] - 3 * x[3] - 6)},
            {'type': 'ineq', 'fun': lambda x: 2 * x[1] + x[3] - 10},
            {'type': 'ineq', 'fun': lambda x: -(-x[0] + 3 * x[2] + x[3] + 3)},
            {'type': 'eq',   'fun': lambda x: x[1] - 5*x[2] - 2*x[3]})
    bounds = ((0, None), (None, None), (0, None), (0, None))

    guess = np.asarray([1, 1, 1, 1])
    result = minimize(func, guess, constraints=cons, bounds=bounds)
    if result.success:
        print(result.x)
