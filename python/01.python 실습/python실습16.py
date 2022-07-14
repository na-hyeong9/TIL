c = 0
s = input()
text = 'a', 'e', 'i', 'o', 'u'
for i in text:
    for j in s:
        if i == j:
            c += 1
print(c)
