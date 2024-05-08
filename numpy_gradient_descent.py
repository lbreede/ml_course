import numpy as np

def gradient_descent(gradient, start, learning_rate, n_iters=50, tolerance=1e-6):
    vector = start
    for _ in range(n_iters):
        diff = -learning_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff

    return vector


gd = gradient_descent(gradient=lambda x: 2*x, start=10.0, learning_rate=0.005, n_iters=2000)
print(gd)
