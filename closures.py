import numpy as np

#memoization

def memo_test():
    cache = {}

    def closure(n):
        if n in cache:
            print("Fetching from cache..")
            return cache[n]

        else:
            print("Calculating process...")
            np.random.seed(42)
            a = np.random.randn(n,n)
            b = np.random.randn(n,n)
            c = np.dot(a,b)
            cache[n] = c
            return c

    return closure

if __name__ == "__main__":

    N = input("Enter the size: ")
    N = int(N)

    matrix_calculation = memo_test()

    m1 = matrix_calculation(N)
    print(m1)

    N = input("Enter the size: ")
    N = int(N)
    m2 = matrix_calculation(N)
    print(m2)

    N = input("Enter the size: ")
    N = int(N)
    m3 = matrix_calculation(N)
    print(m3)

    N = input("Enter the size: ")
    N = int(N)
    m4 = matrix_calculation(N)
    print(m4)
