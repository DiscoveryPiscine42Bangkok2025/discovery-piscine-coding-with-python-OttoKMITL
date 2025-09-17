#!/usr/bin/env python
Input=float(input("Give me a number: "))
if(Input==int(Input)):
    Ceiling=int(Input)
else:
    if(Input>0):
        Ceiling=int(Input)+1
    else:
        Ceiling=int(Input)
print(Ceiling)