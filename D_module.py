"""
File name: Decorator_module.py
Author: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x

Tale modulo contiene le definizioni di profiler e include_stripped.
"""
from time import time, ctime

def include_stripped(decorator):
   """
   Decoratore di decoratori:

   Mantiene il nome originale di func, così che non venga sostituito da quello della
   funzione di wrap.
   """
   def wrapping_decorator(func):
        """
        Nucleo di include_stripped.
        """
        wrapped = decorator(func)
        wrapped_stripped = func
        return wrapped
   return wrapping_decorator

@include_stripped
def profiler(func):
    """
    Decoratore di funzioni.

    Esegue un profiling di func e lo annota nel file log.txt, registrando la data,
    il nome di func, il numero di vertici e archi del grafo di input, il tempo di 
    esecuzione e il valore di ritorno.
    """
    def wrapFunction(*args, **kwargs):
        """
        Nucleo di profiler.
        """
        pathToOutput = "log.txt"
        startTime = time()
#        print(f"startTime is {startTime}")
        
        try:
            rValue = func(args[0], kwargs["debug"])
        except KeyError:
            rValue = func(args[0])

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
