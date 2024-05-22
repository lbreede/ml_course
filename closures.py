import numpy as np
import time


def memo_test():
    cache = {}

    def closure(n):
        if n in cache:
            print("Fetching from cache..")
            return cache[n]

        print("Calculating process...")
        np.random.seed(42)
        a = np.random.randn(n, n)
        b = np.random.randn(n, n)
        c = np.dot(a, b)
        cache[n] = c
        return c

    return closure


if __name__ == "__main__":
    matrix_calculation = memo_test()

    for _ in range(4):
        num = int(input("Enter the size: "))
        start = time.time()
        matrix_calculation(num)
        duration = time.time() - start
        print(f"Matrix calculation with size {num} took {duration:.3f}s")
