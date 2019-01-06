"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Decorator
"""

#from HCUF_module import *
from cProfile import Profile, run
import pstats
import functools
#from Graph.graph.Graph_AdjacencyMatrix import *

#globalParam = None # necessaria per il profiler, altrimenti è impossibile passare il grafo come argomento del decorator.

def include_stripped(decorator):
    def wrapping_decorator(func):
        wrapped = decorator(func)
        wrapped_stripped = func
        return wrapped
    return wrapping_decorator

@include_stripped
def profiler(func):
    def wrapFunction(*args, **kwargs):
        funcProfile = Profile()
        valueReturned = funcProfile.runcall(func, *args, **kwargs)
        funcProfile.dump_stats("tempStats.txt")
        #run(f"{func.__name__}(*args, **kwargs)", "tempStats.txt")
        with open(f"{func.__name__}.txt", 'w') as outPutPath:
            stats = pstats.Stats('tempStats.txt', stream = outPutPath).strip_dirs().sort_stats("time").print_stats()

        return valueReturned
    return wrapFunction

#
#
#@include_stripped
#def profiler(func):
#    @functools.wraps(func)
#    def wrapping_function(args):
#        name = func.__name__
#        global globalParam
#        globalParam = args
#        runctx(f'{name}.stripped(args)', globals(), locals(), 'stats.txt')
#        #run(wrapped_stripped(globalParam), 'stats.txt')
#        with open(f'{name}.txt', 'w') as outPutPath:
#            stats = pstats.Stats('stats.txt', stream = outPutPath).strip_dirs().sort_stats("time")
#            stats.print_stats()
#    return wrapping_function


#@profiler
#def waste_some_time(num_times):
#    for _ in range(num_times):
#        sum([i ** 2 for i in range(10000)])

#if __name__ == "__main__":
#    waste_some_time(1000)
