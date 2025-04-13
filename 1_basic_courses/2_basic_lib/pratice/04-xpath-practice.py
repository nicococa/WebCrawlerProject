import time
from urllib.parse import urljoin
import requests
from lxml import etree

# 爬取荆州58同城房源

if __name__ == '__main__':
    # url = https://jingzhou.58.com/ershoufang/p45/?PGTID=0d000000-0000-0fa7-5199-7aa2860c6577&ClickID=1


    base_url = 'https://jingzhou.58.com/ershoufang'

    cookies = {
        'f': 'n',
        'commontopbar_new_city_info': '3479%7C%E8%8D%86%E5%B7%9E%7Cjingzhou',
        'f': 'n',
        'commontopbar_new_city_info': '3479%7C%E8%8D%86%E5%B7%9E%7Cjingzhou',
        'aQQ_ajkguid': '6B1B0EF3-B717-443A-92B6-399659813C23',
        'sessid': '5FD22DC6-5DDC-4267-8561-A40F8B4FC454',
        'ajk-appVersion': '',
        '58tj_uuid': 'a7f667b8-2b4f-417e-9533-123246567b26',
        'als': '0',
        'xxzlclientid': 'cded41f0-9988-46ff-81e8-1744173755371',
        'xxzlxxid': 'pfmxOJXgTT4WvgSgtilpsgDct67SoqD1GJCs6qey2GzYOECMeePr6BPtQTMvCtycqeHT',
        '58_ctid': '2',
        'is_58_pc': '1',
        'commontopbar_new_city_info': '11%7C%E4%B8%8A%E6%B5%B7%7Csh',
        'id58': 'CkwAWmf7GL5IS1FpDDPEAg==',
        'fzq_h': 'a8a6299c145d30cb4bf741fb7ac9b6a7_1744509123275_c4564c693f614ce4aac905316639055e_3533199343',
        'new_uv': '3',
        'utm_source': '',
        'spm': '',
        'init_refer': '',
        'new_session': '0',
        'city': 'sz',
        '58home': 'sz',
        'ctid': '3479',
        'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjB8MTc0NDUxMDQ3NjEwNDE1ODg1N3xZdmFZYXc5emoyNFh4WkpldHJ3ZGNmV01DTVBQUklMVW1zc3J0Z3I1blcwPXxhZWFmN2FlNmU4NmJiN2ZmMjk0YjA0NjUzMDg4ZDJjNV8xNzQ0NTEwNDc1MzAxX2VjNTNjZjI1OGVlNjQxNWY4YjdmYmZmODkyYWQzMzZjXzM1MzMxOTkzNDN8MDAzMWIwNzMwMWYwOTAxNzVhM2UwYzZiYTliZjVkOWJfMTc0NDUxMDQ3NTM4MF8yNTY=',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,fr-CN;q=0.6,fr;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://jingzhou.58.com/ershoufang/p50/?PGTID=0d000000-0000-0fa7-5199-7aa2860c6577&ClickID=1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        # 'Cookie': 'f=n; commontopbar_new_city_info=3479%7C%E8%8D%86%E5%B7%9E%7Cjingzhou; f=n; commontopbar_new_city_info=3479%7C%E8%8D%86%E5%B7%9E%7Cjingzhou; aQQ_ajkguid=6B1B0EF3-B717-443A-92B6-399659813C23; sessid=5FD22DC6-5DDC-4267-8561-A40F8B4FC454; ajk-appVersion=; 58tj_uuid=a7f667b8-2b4f-417e-9533-123246567b26; als=0; xxzlclientid=cded41f0-9988-46ff-81e8-1744173755371; xxzlxxid=pfmxOJXgTT4WvgSgtilpsgDct67SoqD1GJCs6qey2GzYOECMeePr6BPtQTMvCtycqeHT; 58_ctid=2; is_58_pc=1; commontopbar_new_city_info=11%7C%E4%B8%8A%E6%B5%B7%7Csh; id58=CkwAWmf7GL5IS1FpDDPEAg==; fzq_h=a8a6299c145d30cb4bf741fb7ac9b6a7_1744509123275_c4564c693f614ce4aac905316639055e_3533199343; new_uv=3; utm_source=; spm=; init_refer=; new_session=0; city=sz; 58home=sz; ctid=3479; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjB8MTc0NDUxMDQ3NjEwNDE1ODg1N3xZdmFZYXc5emoyNFh4WkpldHJ3ZGNmV01DTVBQUklMVW1zc3J0Z3I1blcwPXxhZWFmN2FlNmU4NmJiN2ZmMjk0YjA0NjUzMDg4ZDJjNV8xNzQ0NTEwNDc1MzAxX2VjNTNjZjI1OGVlNjQxNWY4YjdmYmZmODkyYWQzMzZjXzM1MzMxOTkzNDN8MDAzMWIwNzMwMWYwOTAxNzVhM2UwYzZiYTliZjVkOWJfMTc0NDUxMDQ3NTM4MF8yNTY=',
    }

    params = {
        'PGTID': '0d000000-0000-0fa7-5199-7aa2860c6577',
        'ClickID': '1',
    }

    # 自己点到最后，发现有50页
    start_time = time.time()
    recordsNum = []
    for pageNum in range(1, 51):
        url = urljoin(base_url, 'ershoufang/p' + str(pageNum))
        response = requests.get('https://jingzhou.58.com/ershoufang/p45/', params=params, cookies=cookies, headers=headers)
        print(response.status_code)

        # response = requests.get('https://jingzhou.58.com/ershoufang/p20/', params=params, cookies=cookies, headers=headers)
        # print(response.status_code)
        # print(response.text)

        tree = etree.HTML(response.text)

        property_contents = tree.xpath('//section[@class="list"]//div[@class="property-content"]')
        # print(property_contents)
        recordsNum.append(len(property_contents))
        for i in range(len(property_contents)):
            property_content_details = property_contents[i].xpath('div[@class="property-content-detail"]')
            # print(property_content_details)

            property_content_title = property_content_details[0].xpath('div/h3/text()')[0]
            # print(property_content_title)
            property_content_info = property_content_details[0].xpath('section/div/p[contains(@class,"property-content-info-text")]/span/text()')
            property_content_info_clean = ''.join(property_content_info)
            # print(property_content_info_clean)

            property_prices = property_contents[i].xpath('div[@class="property-price"]')

            property_price_total = property_prices[0].xpath('p[@class="property-price-total"]/span/text()')
            property_price_total_clean = ''.join(property_price_total)
            # print(property_price_total_clean)

            property_price_average = property_prices[0].xpath('p[@class="property-price-average"]/text()')[0].strip()
            # print(property_price_average)

            # print(property_content_title, property_content_info_clean, property_price_total_clean, property_price_average)
            filename = "../resource/ershoufang.txt"
            with open(filename, 'a', encoding='utf-8') as f:
                total_info = property_content_title + ';' + property_content_info_clean + ";"\
                            + property_price_total_clean + ";" + property_price_average
                f.write(total_info + '\n')

        time.sleep(3)
    print(recordsNum)
    end_time = time.time()
    total_time = end_time - start_time
    print('total time: ', total_time)
