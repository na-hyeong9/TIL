W = int(input())
L = int(input())

if W > 0 and L > 0:
    print(1)
elif W < 0 and L > 0:
    print(2)
elif W < 0 and L < 0:
    print(3)
else:
    print(4)