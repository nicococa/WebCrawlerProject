import re
import string

# 提取出 python
key1 = "java python c++ php"
pattern1 = re.compile(r'python')
res1 = re.findall(pattern1, key1)
print(res1)

# 替换掉_s符号
key2 = 'https://scpic.chinaz.net/files/default/imgs/2023-01-04/610de886ffc6b37d_s.jpg'
pattern2 = re.compile(r'_s')
res2 = re.sub(pattern2, '', key2)
print(res2)

# 提取出hello world
key3 = "<html><h1>hello world</h1><html>"

# 匹配 <h1> 和 </h1> 之间的内容。
# (.*) 表示贪婪匹配任意字符 0 次或多次。
# 所以它希望匹配像 <h1>内容</h1> 这样的结构。
pattern3 = re.compile(r'<h1>(.*)</h1>')
res3 = re.findall(pattern3, key3)
print(res3)

# 提取出170
key4 = '我喜欢身高为170的女生'
# 匹配至少一个数字
pattern4 = re.compile(r'\d+')
res4 = re.findall(pattern4, key4)
print(res4)

# 提取出http:// 和 https://
key5 = 'http://www.baidu.com and https://mi.com'
# s可以出0次或1次
pattern5 = re.compile(r'https?')
res5 = re.findall(pattern5, key5)
print(res5)

# 提取出hello
key6 = 'lalala<hTml>{hello}</HTMl>hahaha'
pattern6 = re.compile(r'<[hH][tT][mM][lL]>{(.*)}</[hH][tT][mM][lL]>')
res6 = re.findall(pattern6, key6)
print(res6)

# 提取出hit.
key7 = 'bobo@hit.edu.cn'
# pattern7 = re.compile(r'\w+@(.*).edu.cn')
# 正则从字符 h 开始匹配（也就是 hit 中的 h）
# .*? 会尽可能少地匹配字符（非贪婪），直到遇到第一个 .（也就是 edu.cn前面的的那个点）
# 所以匹配结果是：hit.
pattern7 = re.compile(r'h.*?\.')
res7 = re.findall(pattern7, key7)
print(res7)

# 提取出saas 和 sas
key8 = 'saas and sas and saaas'
pattern8 = re.compile(r'sa{1,2}s')
res8 = re.findall(pattern8, key8)
print(res8)