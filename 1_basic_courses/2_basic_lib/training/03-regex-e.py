import re

# 用某个字符串替换匹配的内容
# 相当于正则版的 str.replace()

pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")
strings = 'Today is 2018-12-12, the date of the meeting is set at 2019-09-10,\
 please confirm whether to participate before 2018-12-25'

def totype(match):
    return match.group(0).replace('-', '.')

new_strings = re.sub(pattern, totype, strings)

print(new_strings)

strings1 = "I have 2 apples and 10 bananas"
pattern1 = re.compile(r"\d+")
new_strings1 = re.sub(pattern1, 'XXX', strings1)
print(new_strings1)