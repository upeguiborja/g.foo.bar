import solution
import external_solution
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

print('___Solution 1___')
print(f'n=12                | {timeit.timeit(wrapper(solution.solution, "abcabcabcabc"), number=100)}')
print(f'n=240               | {timeit.timeit(wrapper(solution.solution, "abcabcabcabc"*20), number=100)}')
print(f'n=240 (worst case)  | {timeit.timeit(wrapper(solution.solution, "a"*200), number=100)}')
print(f'n=500 (worst case)  | {timeit.timeit(wrapper(solution.solution, "a"*500), number=100)}')
print(f'n=1000 (worst case) | {timeit.timeit(wrapper(solution.solution, "a"*1000), number=100)}')

print('___Solution 2___')
print(f'n=12                | {timeit.timeit(wrapper(external_solution.ext_solution, "abcabcabcabc"), number=100)}')
print(f'n=240               | {timeit.timeit(wrapper(external_solution.ext_solution, "abcabcabcabc"*20), number=100)}')
print(f'n=240 (worst case)  | {timeit.timeit(wrapper(external_solution.ext_solution, "a"*200), number=100)}')
print(f'n=500 (worst case)  | {timeit.timeit(wrapper(external_solution.ext_solution, "a"*500), number=100)}')
print(f'n=1000 (worst case) | {timeit.timeit(wrapper(external_solution.ext_solution, "a"*1000), number=100)}')