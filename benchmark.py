"""Sheet 2 benchmark: compare loop and NumPy matrix multiplication.

Includes a batch timer and configurable repetition counts.
The timer returns a per-call average so the driver can save a CSV.
"""
import csv
import time
import numpy as np

# Change only these settings for the exercise.
SIZES = [5, 10, 20, 40]
REPEATS = 3
LOOPS = 3
SEED = 587


class Timer(object):
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, ty, val, tb):
        self.elapsed = time.time() - self.start
        return False


def our_timer(repeats, loops):
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            for i in range(repeats):
                with Timer() as timer:
                    for j in range(loops):
                        func(*args, **kwargs)
                times.append(timer.elapsed)
            best = min(times)
            print("best of", repeats, "batches of", loops,
                  "calls for", func.__name__, ":", best, "seconds")
            return best / loops
        return wrapper
    return decorator


def matmul_loop(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Inner dimensions must match")
    C = np.zeros((A.shape[0], B.shape[1]), dtype=float)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for r in range(A.shape[1]):
                C[i, j] += A[i, r] * B[r, j]
    return C


@our_timer(REPEATS, LOOPS)
def mult_numpy(A, B):
    return np.dot(A, B)


@our_timer(REPEATS, LOOPS)
def mult_loop(A, B):
    return matmul_loop(A, B)


def main():
    rng = np.random.default_rng(SEED)
    results = []
    for n in SIZES:
        A = rng.random((n, n))
        B = rng.random((n, n))
        if not np.allclose(matmul_loop(A, B), np.dot(A, B)):
            raise ValueError("Results disagree before timing")
        print("Matrix size:", n, "by", n)
        numpy_time = mult_numpy(A, B)
        loop_time = mult_loop(A, B)
        results.append([n, loop_time, numpy_time, loop_time / numpy_time])
    with open("benchmark-results.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["n", "loop_seconds", "numpy_seconds", "speed_ratio"])
        writer.writerows(results)
    print("Saved per-call averages to benchmark-results.csv")


if __name__ == "__main__":
    main()
