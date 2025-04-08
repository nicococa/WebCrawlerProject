import json

import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
        'Cookie': 'route-cell=ksa; VOLCALB=f8d7db5f847ad8400822ae8742f5f6d7|1744083394|1744081370'
    }

    city = input('Enter the city name: ')
    filename = "./response_file/" + city + ".json"

    pageSize = 10
    for i in range(1, 22):
        data = {
            'cname': city,
            'pageIndex': i,
            'pageSize': pageSize
        }
        response = requests.post(url, headers=headers, data=data)
        page_text = response.text
        print(response.text)
        with open(filename, 'a', encoding='utf-8') as f:
            json.dump(page_text, f, ensure_ascii=False)
            f.write('\n')

    print('over')