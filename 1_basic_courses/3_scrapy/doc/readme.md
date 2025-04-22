
安装和启动项目
```
pip3 install scrapy 安装scrapy
scrapy startproject myproject
cd myproject
scrapy genspider demo example.com
例子 
scrapy genspider douban movie.douban.com

scrapy shell "https://movie.douban.com/top250?start=0&filter="
模拟收到了response，然后抓取。
scrapy shell 是用来交互式测试和调试的工具

scrapy crawl douban 启动爬虫


scrapy shell "https://movie.douban.com/top250?start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}
fetch("https://movie.douban.com/top250?start=0", headers=headers)
```
myproject/ 是 Scrapy 项目的目录。
demo.py 是 spider 的主文件。
items.py：定义结构化数据。
pipelines.py：数据处理（比如保存到文件、数据库）。
middlewares.py：请求/响应中间处理器。


project01_example: 第一个scrapy项目用来做演示
