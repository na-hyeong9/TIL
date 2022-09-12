
text = input()
c = []
upper = []


for i in text:
    a = ord(i) 
    c.append(a)
for j in c:
    b = chr(j-32)
    upper.append(b)
print("".join(upper))