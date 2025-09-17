#!/usr/bin/env python
import sys
if(len(sys.argv)>=3):
    Input=sys.argv[1:]
    for i in reversed(Input):
        print(i)
else:
    print("none")