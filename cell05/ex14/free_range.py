#!/usr/bin/env python
import sys
if(len(sys.argv)==3):
    Start=int(sys.argv[1])
    End=int(sys.argv[2])+1
    List=[i for i in range(Start, End)]
    print(List)
else:
    print("none")