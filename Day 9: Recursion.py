"""
Task
Write a factorial function that takes a positive integer,N as a parameter and prints the result
of N!(N factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial,
you will get a score of 0.

Input Format

A single integer,N (the argument to pass to factorial).
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return(n * factorial(n - 1))
print(factorial(10))