import re

# 非字符串字符
pattern = re.compile(r'\W')

# 按照匹配的正则表达式来分割字符串
# 和普通的 str.split() 类似，但支持正则规则。

strings = 'This$is&the@largest&ball'
result = re.split(pattern, strings)
print(result)

pattern1 = "apple,banana;orange|grape"
# 按照逗号、分号或竖线分割
result1 = re.split(r"[,;|]", pattern1)
print(result1)