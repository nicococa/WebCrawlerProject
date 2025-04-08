import json

import requests

if __name__ == '__main__':
    post_url = 'https://httpbin.org/post'

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    word = input('enter a word: ')
    data = {
        'input': word,
    }

    response = requests.post(url=post_url, headers=headers, data=data)
    print(response.text)
    print(response.json())

    filename = './response_file/' + word + '.json'

    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(response.json(), fp=fp, ensure_ascii=False, indent=4)

    print('file saved to {}'.format(filename))