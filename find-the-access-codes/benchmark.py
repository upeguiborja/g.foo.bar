import random
import alternative
import solution
import timeit

def printMatrix(M):
    print("Matrix: {")
    for row in M:
        print(row)
    print("}")

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

problem = [2]*500
s1 = wrapper(alternative.solution, problem)
s2 = wrapper(solution.solution, problem)
s3 = wrapper(alternative.solution2, problem)

print("Running...")
print("Worst case scenario: upper triangular all 1s")
print(f"Alternative O[n^3] with optimizations: {timeit.timeit(s1, number=100)}, Result: {alternative.solution(problem)}")
print(f"Graph walk solution with O[n^2]: {timeit.timeit(s2, number=100)}, Result: {solution.solution(problem)}")
print(f"misha-lavrov suggestion with O[n^2]: {timeit.timeit(s3, number=100)}, Result: {alternative.solution2(problem)}")
print("--- Done ---")
