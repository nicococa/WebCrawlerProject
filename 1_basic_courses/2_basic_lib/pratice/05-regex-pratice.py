import re
from urllib.parse import urljoin
import requests

# 用正则表达式爬取豆瓣高分电影的图片和标题
if __name__ == '__main__':

    cookies = {
        'cf_clearance': 'XPuJISAWWgo8BS.GjxthuEQ4wqEvpA.da9iJUsLT9VQ-1744550960-1.2.1.1-n.D0pWF7aq.H_2riGI.AkVK0c5qy9Z2TAYdsIPMCsRVHcS.AldX9SxLqTMX.fOTfrkzLDAwFCCQQ_ikL.90zdyOIcbXziemhC3PIyUNAjUvgr3t1t.ozxxbpwvIzZElYSxlZ.waUMsCyohAMVXecNOIX52hsXYtkQueZoJuqbr1Gc_MQ6nFChNXPI6FwAfUIMheTKLgHHy98IPkGX53RdLk9PZGqqJipNMH6Rqu2iOYLZKrQ7RWxiQiREtXXJseHwUIgW0DrZpm8NgiCKn_LGw6GMT5EKPmkyd7qmviwd80OIDCYcAZQaJWDOcGjhKB7vtFu5EzzTPM_hjyu.U_85yjUGSh6I9fTVsfOq3.8XCQRNBaqXPZZgox9o6xk56Hz',
        'zkhanecookieclassrecord': '%2C58%2C',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,fr-CN;q=0.6,fr;q=0.5',
        'priority': 'u=0, i',
        'referer': 'https://pic.netbian.com/4kdongwu/index_8.html',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-arch': '"arm"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"135.0.7049.85"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.85", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.85"',
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
        # 'cookie': 'cf_clearance=XPuJISAWWgo8BS.GjxthuEQ4wqEvpA.da9iJUsLT9VQ-1744550960-1.2.1.1-n.D0pWF7aq.H_2riGI.AkVK0c5qy9Z2TAYdsIPMCsRVHcS.AldX9SxLqTMX.fOTfrkzLDAwFCCQQ_ikL.90zdyOIcbXziemhC3PIyUNAjUvgr3t1t.ozxxbpwvIzZElYSxlZ.waUMsCyohAMVXecNOIX52hsXYtkQueZoJuqbr1Gc_MQ6nFChNXPI6FwAfUIMheTKLgHHy98IPkGX53RdLk9PZGqqJipNMH6Rqu2iOYLZKrQ7RWxiQiREtXXJseHwUIgW0DrZpm8NgiCKn_LGw6GMT5EKPmkyd7qmviwd80OIDCYcAZQaJWDOcGjhKB7vtFu5EzzTPM_hjyu.U_85yjUGSh6I9fTVsfOq3.8XCQRNBaqXPZZgox9o6xk56Hz; zkhanecookieclassrecord=%2C58%2C',
    }

    #
    # response = requests.get('https://pic.netbian.com/4kdongwu/index_3.html', cookies=cookies, headers=headers)
    # response.encoding = "gbk"
    filename = "../resource/03-regex-pratice.html"

    # 保存在本地用来验证
    # with open(filename, 'w', encoding='utf-8') as f:
    #     f.write(response.text)
    # print(response.status_code)


    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        # print(content)

    pattern = re.compile(r'<li.*?<img src="(.*?)" alt="(.*?)".*?>')
    res = re.findall(pattern, content)
    for index in range(len(res)):
        #  修改文件名
        img_name = res[index][1].replace(" ", "_").replace("/", "_") + ".jpg"

        base_url = "https://pic.netbian.com/"
        img_url = urljoin(base_url, res[index][0])
        print(img_url)
        img_saved_location = "../resource/images/" + img_name
        img_response = requests.get(img_url, cookies=cookies, headers=headers)
        if img_response.status_code == 200:
            with open(img_saved_location, "wb") as f:
                f.write(img_response.content)
            print(f'{img_name} 下载成功')
        else:
            print(f'{img_name} 下载失败')
    print("over")

