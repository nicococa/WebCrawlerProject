# UA检测（反爬机制）：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份为某一浏览器，说明该请求是一个正常请求。
# 但是如果检测到不是某一浏览器，则表示该请求为非正常请求。服务器端拒绝该次请求。
# UA：User-Agent（请求载体的身份标识）
# UA伪装：让爬虫身份标识伪装成浏览器
# 解决办法：在请求头中添加对应的header

import requests

if __name__ == "__main__":
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = "https://www.sogou.com/web?"
    # 处理url携带的参数：封装到字典中
    kw = input('enter keyword: ')
    params = {
        'query': kw,
    }

    # 不带user-agent，可以对比带上user-agent的服务器返回的数据
    # response_without_headers = requests.get(url, params=params)
    # page_txt = response_without_headers.text

    # 带上user-agent
    response_with_headers = requests.get(url, params=params, headers=headers)
    page_txt = response_with_headers.text

    print(page_txt)
    filename = './response_file/' + kw + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_txt)
    print(filename, '保存成功')