#!/usr/bin/env python
import sys
if(len(sys.argv)!=1):
    for i in sys.argv[1:]:
        if not i.endswith("ism"):
            i+="ism"
            print(i)
else:
    print("none")