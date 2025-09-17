#!/usr/bin/env python
import sys
def downcase_it(Input):
    return Input.lower()
if(len(sys.argv)!=1):
    for i in sys.argv[1:]:
        print(downcase_it(i))
else:
    print("none")