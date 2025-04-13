import time
from lxml import etree
import requests
import os
from urllib.parse import urljoin

if __name__ == '__main__':
    # 这个很重要，需要复制全部header，需要网站是在发送get请求的header
    cookies = {
        'zkhanecookieclassrecord': '%2C60%2C',
        'cf_clearance': '3O9MmijWYDQgTAwK4aH7LLKrl2iUP.QlexdvmEXthjQ-1744508765-1.2.1.1-T_mchREp7KYUBgUrWqO8HknMGCg.9V4ziBo4ZJPREudrDhgrFVjgYfCMyphuv4Z0W04RtRys159SMdCkF3x54naeah0brF9Dq1YJylqM_jKJzNOth9j2SHylLy7v7dWixD.CbuTpqQ2WZj3kum66YWvBboz9E3D.MxMNPS0yi1u0Cj3IjvjrzBbHo2pjZyPLv6sXZB9_6MvWLH5lKkO7inSDjFD2zUzJYK58hJgJ.WYlUs51r1.G18gkEPnNkODSELXCBT8Dvt1iyVwxulxcqxGlLhaB2Px6HwaXzsMNVIiuu09g3gq7JgcivUUZmS8AULyBdNMLEXhLnzTtXctLnH2qnfybMJLyjydYff1t2AEeWx2kX7Aw8pmqyvSYFgtT',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,fr-CN;q=0.6,fr;q=0.5',
        'priority': 'u=0, i',
        'referer': 'https://pic.netbian.com/4kyingshi/index_17.html',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-arch': '"arm"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"135.0.7049.84"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.84", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.84"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"15.3.2"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        # 'cookie': 'zkhanecookieclassrecord=%2C60%2C; cf_clearance=3O9MmijWYDQgTAwK4aH7LLKrl2iUP.QlexdvmEXthjQ-1744508765-1.2.1.1-T_mchREp7KYUBgUrWqO8HknMGCg.9V4ziBo4ZJPREudrDhgrFVjgYfCMyphuv4Z0W04RtRys159SMdCkF3x54naeah0brF9Dq1YJylqM_jKJzNOth9j2SHylLy7v7dWixD.CbuTpqQ2WZj3kum66YWvBboz9E3D.MxMNPS0yi1u0Cj3IjvjrzBbHo2pjZyPLv6sXZB9_6MvWLH5lKkO7inSDjFD2zUzJYK58hJgJ.WYlUs51r1.G18gkEPnNkODSELXCBT8Dvt1iyVwxulxcqxGlLhaB2Px6HwaXzsMNVIiuu09g3gq7JgcivUUZmS8AULyBdNMLEXhLnzTtXctLnH2qnfybMJLyjydYff1t2AEeWx2kX7Aw8pmqyvSYFgtT',
    }

    base_url = 'https://pic.netbian.com/'

    # 保存目录的路径
    save_dir = "../resource/images"
    os.makedirs(save_dir, exist_ok=True)

    session = requests.Session()

    # 记录每页保存了多少个
    number_record = []
    start_time = time.time()
    for i in range(1, 50):
        if i == 1:
            url = urljoin(base_url, '4kyingshi/index.html')
        else:
            path = base_url + '4kyingshi/index_' + str(i) + '.html'
            url = urljoin(base_url, path)
        print(url + ' is being scraped')
        response = session.get(url, cookies=cookies, headers=headers)
        print(response.status_code)
        response.encoding = "gbk"
        if response.status_code != 200:
            break
        print(f'{url} is being scraped {response.status_code}')


        tree = etree.HTML(response.text)
        img_tags = tree.xpath('//div[@class="slist"]/ul/li/a/img')
        number_record.append(len(img_tags))
        for img in img_tags:
            img_src = img.get('src')
            img_name = img.get("alt", "unnamed").replace(" ", "_").replace("/", "_") + ".jpg"
            img_url = base_url + img_src
            response = session.get(img_url, cookies=cookies, headers=headers)
            if response.status_code == 200:
                with open(os.path.join(save_dir, img_name), 'wb') as f:
                    f.write(response.content)
                print(img_name + ' is being scraped')
            else:
                print(img_name + ' is NOT being scraped')

        time.sleep(3)
    end_time = time.time()  # 结束时间

    total_time = end_time - start_time
    print(f"总耗时: {total_time:.2f} 秒")
    print(f"total record: {len(number_record)}")
    print(number_record)
    # 总数和文件数对不上是因为可能有重复的文件，没有进行判断
    print('all done')
