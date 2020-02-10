"""
Task
Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-10 integer
denoting the maximum number of consecutive 1's in n's binary representation.

Sample Input 1
5
Sample Output 1
1

Sample Input 2
13
Sample Output 2
2

Explanation

Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of  is 13, 1101 so the maximum number of consecutive 1's is 2.
"""

def convertBinaryNum(n):
  # Count max consecutive 1s
    maxCon = 0
  # Count cosecutive 1s
    countCon = 0

    while n > 0:
        remainder = n % 2
        if remainder == 1:
            countCon += 1
            if countCon > maxCon:
                maxCon = countCon
        else:
            countCon = 0
        n = n // 2
    return maxCon


if __name__ == '__main__':
    n = int(input())
    print(convertBinaryNum(n))