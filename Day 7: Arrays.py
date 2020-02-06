"""
Task

Given an array, A, of N integers, print A's elements in reverse order as a single
line of space-separated numbers.
"""

input()

a = str(input()).split(" ")
a.reverse()
for n in a:
  print(n + " ", end="")
