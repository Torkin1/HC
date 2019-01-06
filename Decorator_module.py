"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Decorator
"""

from HCUF_module import *
from cProfile import run
import pstats
import functools

def include_original(dec):
    def meta_decorator(f):
        decorated = dec(f)
        decorated._original = f
        return decorated
    return meta_decorator

@include_original
def time(func):
    @functools.wraps(func)
    def wrapping_function():
        run('waste_some_time._original()', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        #value = pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        #elapsed = 500
        #print(f'Function {func.__name__} with args {args} took {elapsed} seconds')
        #return value
        #filename = 'test.txt'
        #run('waste_some_time()', "stats.txt")
        #stats = pstats.Stats("stats.txt")
        #stats.strip_dirs().sort_stats('time').print_stats()
        #pr.dump_stats(filename)

        #return value

    wrapping_function._original = func
    return wrapping_function



@time
def waste_some_time():
    print("waste_some_time called")
    for i in range(5000):
        sum([i ** 2 for i in range(10000)])

if __name__ == "__main__":
    waste_some_time()

