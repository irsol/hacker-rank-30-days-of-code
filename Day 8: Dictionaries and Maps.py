"""
Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective
phone numbers. You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form 
name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

n = int(input())
phoneBook = {}

# Fill a phonebook
for i in range(0, n):
  entry = str(input()).split(" ")
  name = entry[0]
  number = entry[1]  
  phoneBook[name] = number
  
# Use while loop because don't know how many name entries will be
while True:
    try:
        name = input()
    except:
        break
    if name in phoneBook:
        number = phoneBook[name]
        print(name + "=" + number)
    else:
        print("Not found")