def r (a, b):
    area = a * b
    round = (a + b)*2
    return area, round
a, b = map(int,input(). split())
print(r(a, b))