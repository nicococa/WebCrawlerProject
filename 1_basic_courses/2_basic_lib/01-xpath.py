import os

from lxml import etree

if __name__ == '__main__':
    # 获得当前路径
    # print(os.getcwd())
    tree = etree.parse('./resource/01-xpath-test.html')

    # 绝对路径 从根节点开始，逐级定位
    # r = tree.xpath('/html/body')

    # 从当前节点出发，寻找它的直接子节点（不是后代节点）
    # r = tree.xpath('body')

    # 根节点出发，到了html之后，寻找所有的p
    # r = tree.xpath('/html//p')

    # 找到所有的div元素，其中他的class名为song
    r = tree.xpath('//div[@class="song"]')

    print(r)