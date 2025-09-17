#!/usr/bin/env python
import sys
if(len(sys.argv)==2 and 'z' in sys.argv[1]):
    Input=sys.argv[1]
    for i in Input:
        if(i=='z'):
            print(i, end="")
else:
    print("none")