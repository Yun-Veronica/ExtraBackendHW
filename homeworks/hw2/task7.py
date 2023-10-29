a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c

if a != 0:
    if d > 0:
        x1 = (-1 * b - (d) ** 0.5) / (2 * a)
        x2 = (-1 * b + (d) ** 0.5) / (2 * a)
        print(x1, x2)
    elif d == 0:
        x = -1 * b / (2 * a)
        print(x)
