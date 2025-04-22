# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Project01ExamplePipeline:
    def process_item(self, item, spider):
        title = item.get('title', '').strip()
        score = item.get('score', '').strip()
        motto = (item.get('motto') or '').strip()

        # 确保文件夹存在，如果不存在则创建
        folder_path = 'data'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(os.path.join(folder_path, 'output.txt'), 'a', encoding='utf-8') as f:
            line = f"{title} {score} {motto}\n"
            f.write(line)

        return item
