#!/usr/bin/env python
Input=int(input("Enter a number less than 25\n"))
if(Input>25):
    print("Error")
else:
    while(Input<=25):
        print(f"Inside the loop, my variable is {Input}")
        Input+=1