import requests
from lxml import etree

# 爬取的fake agents

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    url = 'https://useragentstring.com/pages/Firefox/'
    response = requests.get(url, headers=headers)
    # print(response.text)
    tree = etree.HTML(response.text)


    elem = tree.xpath('//h4 | //ul')
    filename = '../resource/01-xpath-test.txt'

    pairs = []
    for i in range(0, len(elem), 2):  # 步长为 2
        elem_h4 = elem[i]
        elem_ul = elem[i + 1]
        elem_h4_text = elem_h4.text
        elem_all_li_a_text = elem_ul.xpath('li/a/text()')
        # print(elem_h4.text)
        # print(elem_all_li_a_text)
        with open(filename, 'a', encoding='utf-8') as fp:
            fp.write(elem_h4_text + '\n')
            for li_a_text in elem_all_li_a_text:
                fp.write(li_a_text + '\n')
            fp.write('\n')

    print("Over")
