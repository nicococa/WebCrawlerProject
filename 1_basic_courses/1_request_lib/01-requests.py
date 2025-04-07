# 引用测试Requests库

import requests

if __name__ == "__main__":
    # 指定url
    url = "https://news.sina.com.cn/"
    # 发起请求
    response = requests.get(url)
    # 获取相应数据
    page_txt = response.text
    print(page_txt)
    # 持久话存储
    with open('./response_file/xina.html', 'w', encoding='utf-8') as fp:
        fp.write(page_txt)
    print('爬取结束')
