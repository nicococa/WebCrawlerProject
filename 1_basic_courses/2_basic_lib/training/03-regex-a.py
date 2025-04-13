import re

#将正则表达式转化为Pattern对象
# 匹配的应该为0000-88888888
pattern = re.compile(r'(\d{4})-(\d{8})')

# 带匹配字符串
string1 = "0755-44445555 is our new o f fi c e phone number"
string2 = "the old number 0755-11112222 is no longer used"


## re.match
# 直接用一个正则表达式匹配某个字符串的 开头，如果匹配成功，返回匹配对象，否则返回 None。
match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)

if match1:
    print(type(match1))
    print(match1.groups()) #('0755', '44445555') 所有匹配结果
    print(match1.group(0)) # 0755-44445555 未分组的原始匹配对象
    print(match1.group(1)) # 0755 第一组对象
    print(match1.group(2)) # 44445555 第二组对象
else:
    print('match1 未匹配到对象')

if match2:
    print(type(match2))
    print(match2.groups())
    print(match2.group(0))
    print(match2.group(1))
    print(match2.group(2))
else:
    print('match2 未匹配到对象')

