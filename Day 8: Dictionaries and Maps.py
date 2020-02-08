"""
Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective
phone numbers. You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form 
name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

n = int(input())
phoneBook = dict()

for i in range(0, n):
  name, number = input().split()
  phoneBook[name] = number

for j in range(0, n):
  name = input()
  if name in phoneBook:
      print("{}={}".format(name, phoneBook[name]))
  else:
      print("Not found")