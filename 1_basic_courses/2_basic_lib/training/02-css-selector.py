from bs4 import BeautifulSoup


if __name__ == "__main__":
    with open('../resource/02-css-selector-test.html') as fp:
        soup = BeautifulSoup(fp, 'lxml')
        # 打印出这个 HTML 文件解析后的完整结构，就是类似于格式化后的 HTML 文本。
        # print(soup)

        # print(soup.h1) # 返回第一个html中的h1元素
        # print(soup.find('div')) # 想当于soup.div
        # print(soup.find('ul', class_='items')) #找到第一个class为items的ul元素

        # print(soup.find('li'))
        # print(soup.find_all('li'))
        # print(soup.find_all('li')[0])

        # print(soup.select('#main-title + p.intro'))
        # print(soup.select('html div > p + ul.items > li'))
        # print(soup.select('html div > p + ul.items > li')[0])

        # print(soup.select('html div > p + ul.items > li')[0].text)
        # print(soup.select('html div > p + ul.items > li')[0]['class'])

        print(soup.select('a'))
        print(soup.a)
        print(soup.select('a')[0]['href'])
        print(soup.select('a')[0]['target'])
