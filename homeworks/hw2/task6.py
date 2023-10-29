a = int(input())
b = int(input())
c = int(input())

# # простой способ
# l = [a, b, c]
# print(sorted(l))

# используя условные операторы
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
