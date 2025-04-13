import time

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    basic_url = 'https://www.shicimingju.com/book/sanguoyanyi/'
    start_time = time.time()
    for page_index in range(1, 121):
        url = basic_url + str(page_index) + '.html'
        # print(url)
        response = requests.get(url, headers=headers)
        # 把 response.text 的编码手动设置为自动检测到的编码，防止乱码
        response.encoding = response.apparent_encoding

        if response.status_code == 200:
            # 用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(response.text, 'lxml')
            # print(soup)
            title = soup.select('html div.main h1.bt')[0].text
            # print(soup.select('html div.main h1.bt'))
            print(title)
            p_element = soup.select('html div.main div.text.p_pad p')
            # print(soup.select('html div.main div.text.p_pad p'))
            contents_arr = [p.text.replace('&nbsp;', ' ').strip() for p in p_element]
            contents = "".join(contents_arr)
            # print(contents)

            filename = "../resource/sanguoyanyi.txt"
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(title + '\n')
                f.write(contents)
                f.write('\n')
        time.sleep(3)

    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    print("over")

