#!/usr/bin/env python
def greetings(Name="noble stranger"):
    if isinstance(Name, str):
        print(f"Hello, {Name}.")
    else:
        print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)