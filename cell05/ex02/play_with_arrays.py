#!/usr/bin/env python
List=[2, 8, 9, 48, 8, 22, -12, 2]
print(List)
for i in range(len(List)):
    List[i]+=2
Listt=[i for i in List if i>5]
print(Listt)