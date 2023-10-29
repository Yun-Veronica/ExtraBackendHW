n = int(input())

h = 9
m = n * 45
if n % 2 == 0 and n > 1:
    m += (n // 2) * 5
    m += ((n // 2) - 1) * 15
elif n % 2 != 0 and n > 1:
    m += ((n - 1) // 2) * 15
    m += ((n - 1) // 2) * 5

h += m // 60
m -= (m // 60) * 60
print(h, m)
