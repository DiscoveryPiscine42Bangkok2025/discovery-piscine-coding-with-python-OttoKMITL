#!/usr/bin/env python
import sys
if(len(sys.argv)==2):
    Word=sys.argv[1]
    Input=input("What was the parameter? ")
    if(Word==Input):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")