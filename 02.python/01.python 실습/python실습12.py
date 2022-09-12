text = 'apple'
new_text = text.replace('a','')
print(new_text)

# 반복문을 통한 'a'지우기
str = 'apple'
result = str
for char in str:
    if char in 'a':
        result=result.replace(char,'')
print(result)