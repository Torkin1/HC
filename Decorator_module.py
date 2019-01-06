"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Decorator
"""

from cProfile import run
import pstats
import functools

def include_stripped(decorator):
    def wrapping_decorator(func):
        wrapped = decorator(func)
        wrapped.stripped = func
        return wrapped
    return wrapping_decorator


@include_stripped
def profiler(func):
    @functools.wraps(func)
    def wrapping_function(*args, **kwargs):
        name = func.__name__
        param = int(args[0])
        run(f'{name}.stripped({param})', 'stats.txt')
        with open(f'{name}.txt', 'w') as outPutPath:
            stats = pstats.Stats('stats.txt', stream = outPutPath).strip_dirs().sort_stats("time")
            stats.print_stats()
    return wrapping_function


@profiler
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])
if __name__ == "__main__":
    waste_some_time(100)