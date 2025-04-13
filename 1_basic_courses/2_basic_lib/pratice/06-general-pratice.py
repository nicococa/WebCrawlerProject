import time
from urllib.parse import urljoin

import requests
import os
from lxml import etree

if __name__ == '__main__':
    start_time = time.time()

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    base_url = 'https://sc.chinaz.com/jianli/'
    total_record = 0
    # 肉眼观察共有965个页面
    for pageNumber in range(1, 51):
        if pageNumber == 1:
            url = urljoin(base_url, 'free.html')
        else:
            path = 'free_' + str(pageNumber) +'.html'
            url = urljoin(base_url, path)
        response = requests.get(url, headers=headers)
        # 需要解码先，不然全是字节，无法阅读
        print(url)
        html = response.content.decode('utf-8')
        tree = etree.HTML(html)
        img_elems = tree.xpath('//div[@id="main"]/div/div/a/img')

        for index in range(len(img_elems)):
            img_url = 'https:' + img_elems[index].attrib['src']
            img_name = img_elems[index].attrib['alt'].replace(" ", "_").replace("/", "_")
            img_save_name = '../resource/images/' + img_name + '.jpg'
            # print(img_url)
            # print(img_name)
            img_response = requests.get(img_url, headers=headers)
            # time.sleep(1)
            if img_response.status_code == 200:
                with open(img_save_name, 'wb') as f:
                    f.write(img_response.content)
                total_record = total_record + 1
                print(f'{img_save_name} download ok')
            else:
                print(f'{img_save_name} download failed')


    end_time = time.time()
    total_time = end_time - start_time
    print("over")
    print("total record:", total_record)
    print("total time:", total_time)
