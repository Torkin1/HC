"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Decorator
"""

#from cProfile import Profile, run
#import pstats
from time import time, ctime

def include_stripped(decorator):
    
    def wrapping_decorator(func):
        
        wrapped = decorator(func)
        wrapped_stripped = func
        return wrapped
    return wrapping_decorator

@include_stripped
def profiler(func):

    def wrapFunction(*args, **kwargs):

        pathToOutput = "log.txt"
        startTime = time()
#        print(f"startTime is {startTime}")
        
        try:
            rValue = func(args[0], kwargs["debug"])
        except KeyError:
            rValue = func(args[0])

#        try:
#            if kwargs["timeAccuracy"] >= 0:
#                timeAccuracy = 3 + kwargs["timeAccuracy"]
#        except KeyError:
#                timeAccuracy = 3
        
        #endTime = time()
        #print(f"endTime is {endTime}")
        elapsedTime = time() - startTime
        appendedLine = f"[{ctime(time())}] name: {func.__name__} ; nodes: {len(args[0].adj)} ; edges: {args[0].numEdges()} ; elapsed: {'%.3f' % elapsedTime}s ; return: {rValue}\n"
        with open(pathToOutput, "a") as fOutput:
            
            fOutput.write(appendedLine)
        
        try:
            if kwargs["showProfile"]:
                print(appendedLine)
        except KeyError:
            pass
        
        return rValue
    
    return wrapFunction
            
#@include_stripped
#def profiler(func):
#    
#    def wrapFunction(*args, **kwargs):
#        
#        funcProfile = Profile()
#        pathToOutput = f"{func.__name__}" + f"{len(args[0].adj)}" + ".txt"
#        
#        valueReturned = funcProfile.runcall(func, *args, **kwargs)
#        funcProfile.dump_stats("tempStats.txt")
#        
#        with open(pathToOutput, 'w') as fOutput: 
#            fOutput.write(f"Function called: {func.__name__}\n")
#            fOutput.write("\n")
#            fOutput.write(f"Size of input: {len(args[0].adj)} nodes, {args[0].numEdges()} edges\n")
#            fOutput.write("\n")
#            pstats.Stats('tempStats.txt', stream = fOutput).strip_dirs().sort_stats("time").print_stats()
#        
#        return valueReturned
#    return wrapFunction

