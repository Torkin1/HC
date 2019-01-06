"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Decorator
"""

from cProfile import Profile, run
import pstats

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
        pathToOutput = f"{func.__name__}" + f"{len(args[0].adj)}" + ".txt"
        
        valueReturned = funcProfile.runcall(func, *args, **kwargs)
        funcProfile.dump_stats("tempStats.txt")
        #run(f"{func.__name__}(*args, **kwargs)", "tempStats.txt")
        
        with open(pathToOutput, 'w') as fOutput: 
            fOutput.write(f"Function called: {func.__name__}\n")
            fOutput.write("\n")
            fOutput.write(f"Size of input: {len(args[0].adj)} nodes, {args[0].numEdges()} edges\n")
            fOutput.write("\n")
            pstats.Stats('tempStats.txt', stream = fOutput).strip_dirs().sort_stats("time").print_stats()
        
        return valueReturned
    return wrapFunction

