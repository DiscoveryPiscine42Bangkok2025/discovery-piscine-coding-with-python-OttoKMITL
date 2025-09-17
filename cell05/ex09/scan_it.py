#!/usr/bin/env python
import sys
import re
if(len(sys.argv)==3):
    Input1=sys.argv[1]
    Input2=sys.argv[2]
    Match=re.findall(re.escape(Input1), Input2)
    if Match:
        print(len(Match))
    else:
        print("none")
else:
    print("none")