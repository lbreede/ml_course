from numba import cuda
import numpy as np
import math
import time


@cuda.jit
def matmul_kernel(matrix_a, matrix_b, matrix_c):
    """Perform matrix multiplication of C = A * B"""
    shared_a = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    shared_b = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x

    if x >= matrix_c.shape[0] and y >= matrix_c.shape[1]:
        return

    tmp = 0
    for i in range(bpg):
        shared_a[tx, ty] = matrix_a[x, ty + i * TPB]
        shared_b[tx, ty] = matrix_b[tx + i * TPB, y]
        cuda.syncthreads()

        for j in range(TPB):
            tmp += shared_a[tx, j] * shared_b[j, ty]
        cuda.syncthreads()

    matrix_c[x, y] = tmp


N = 512
TPB = 8

start_time = time.monotonic()

a_matrix = np.random.rand(N, N).astype(np.float32)
b_matrix = np.random.rand(N, N).astype(np.float32)
c_matrix = np.zeros((N, N)).astype(np.float32)

# d_a_matrix = cuda.to_device(a_matrix)
# d_b_matrix = cuda.to_device(b_matrix)
# d_c_matrix = cuda.to_device(c_matrix)

threadsperblock = (TPB, TPB)
blockspergrid_x = int(math.ceil(a_matrix.shape[0] / threadsperblock[1]))
blockspergrid_y = int(math.ceil(b_matrix.shape[1] / threadsperblock[0]))
blockspergrid = (blockspergrid_x, blockspergrid_y)

matmul_kernel[blockspergrid, threadsperblock](a_matrix, b_matrix, c_matrix)

end = time.monotonic()

print(f"Time: {end - start_time}")
print(c_matrix)
