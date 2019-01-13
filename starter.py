"""
File name: profiler.py
Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Script di profiling per la creazione e analisi dei grafi
"""

import argparse
import GG_module
import HCUF_module
import HCDFS_module

if __name__ == "__main__":

    parser = argparse.ArgumentParser("$ python3 -m starter",
                                     epilog="written by Mihai Jianu, Daniele La Prova, Lorenzo Mei",
                                     description="profiles the HCUF_module, HCDFS_module")
    parser.add_argument("nodes", type=int, help="insert the number of Nodes to be put on the generator")
    parser.add_argument("range", type=int, help="maximum range of values generated")
    parser.add_argument("-d", "--debug", help="Print all the actions that the alghoritms dofor an easier debugging", action="store_true")
    parser.add_argument("-s", "--showProfile", help="Show on console the execution time", action="store_true")
    args = parser.parse_args()

    G = GG_module.gGenerator(args.nodes, args.range, args.debug, args.showProfile)
    #HCUF_module.hasCycleUF(G, debug = args.debug, showProfile = args.showProfile)
    #HCDFS_module.hasCycleDFS(G, debug = args.debug, showProfile = args.showProfile)
    #if type(G) != None:
    #    HCUF_module.hasCycleUF(G, debug = False, showProfile = False)
    #   HCDFS_module.hasCycleDFS(G, debug = False, showProfile = False)
    HCUF_module.hasCycleUF(G, args.debug, args.showProfile)
    HCDFS_module.hasCycleDFS(G, args.debug, args.showProfile)

