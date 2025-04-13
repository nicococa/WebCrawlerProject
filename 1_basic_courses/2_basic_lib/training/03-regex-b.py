import re

#将正则表达式转化为Pattern对象
# 匹配的应该为0000-88888888
pattern = re.compile(r'(\d{4})-(\d{8})')

# 带匹配字符串
string1 = "0755-44445555 is our new o f fi c e phone number"
string2 = "the old number 0755-11112222 is no longer used"

### re.search
# 在字符串中查找第一个匹配正则表达式的内容，如果找到返回匹配对象，否则返回 None
search1 = re.search(pattern, string1)
search2 = re.search(pattern, string2)

if search1:
    print(type(search1))
    print(search1.groups())
    print(search1.group())
    print(search1.group(0))
    print(search1.group(1))
    print(search1.group(2))
else:
    print('search1 未匹配到对象')

if search2:
    print(type(search2))
    print(search2.groups())
    print(search2.group(0))
    print(search2.group(1))
    print(search2.group(2))
else:
    print('search2 未匹配到对象')