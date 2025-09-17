#!/usr/bin/env python
FirstNumber=int(input("Enter the first number:\n"))
SecondNumber=int(input("Enter the second number:\n"))
Product=FirstNumber*SecondNumber
print(f"{FirstNumber} x {SecondNumber} = {Product}")
if(Product>0):
    print("The result is positive.")
if(Product==0):
    print("The result is positive and negative.")
if(Product<0):
    print("The result is negative.")