# There is a string, s, of lowercase English letters that is repeated infinitely many times.
# Given an integer, n, find and print the number of letters a's in the first n letters of the
# infinite string

# Example
# s = 'abcac'
# n = 10
# The substring that we consider is abcacabcac, the first 10 characters of the infinite string.
# There are 4 occurrences of a in the substring

def repeatedString(s, n):
    # Write your code here
    total = 0
    for i in s:
        if i == 'a':
            total += 1
    total = n//len(s) * total

    for i in s[:n % len(s)]:
        if i == 'a':
            total += 1
    return total


print(repeatedString('abcac', 10))
