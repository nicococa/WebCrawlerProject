import requests

url = 'https://movie.douban.com/top250?'

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

start = input('input a number: ')

params = {
    'start': start,
}

response = requests.get(url, params=params, headers=headers)
print(response.text)

filename = './response_file/doubanTop' + start + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(response.text)

print("over")