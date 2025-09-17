#!/usr/bin/env python
import sys
def shrink(Input):
    print(Input[:8])
def enlarge(Input):
    print(Input+('z'*(8-len(Input))))
if(len(sys.argv)!=1):
    for i in sys.argv[1:]:
        if(len(i)>8):
            shrink(i)
        if(len(i)<8):
            enlarge(i)
        if(len(i)==8):
            print(i)
else:
    print("none")