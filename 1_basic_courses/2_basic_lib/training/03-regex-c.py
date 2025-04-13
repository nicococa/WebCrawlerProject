import re

# 在字符串中找到所有符合正则表达式的内容，并返回一个列表。
pattern = re.compile(r'\d+')
strings = 'Your activation code is 73829-72993-00983-84721'

result = re.findall(pattern, strings)
print(result)


pattern1 = re.compile(r'(\d{3})-(\d{4})')
strings1 = "My phone number is 123-4567 and office number is 987-6543"
result1 = re.findall(pattern1, strings1)
print(result1) #[('123', '4567'), ('987', '6543')]
print(result1[0][0])