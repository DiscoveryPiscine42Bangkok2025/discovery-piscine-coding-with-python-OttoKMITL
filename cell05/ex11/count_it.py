#!/usr/bin/env python
import sys
if(len(sys.argv)==1):
    print("none")
else:
    Input=sys.argv[1:]
    print(f"parameters: {len(Input)}")
    for i in Input:
        print(f"{i}: {len(i)}")