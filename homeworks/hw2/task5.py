n = int(input())
n2 = int(input())
n3 = int(input())

count_same = 0

if n == n2 and n2 == n3 and n == n2:
    count_same = 3
elif n == n2 or n2 == n3 or n == n2 or n == n3:
    count_same = 2

print(count_same)
