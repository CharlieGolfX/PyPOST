import requests
import random
import time

count = 0
wordlist = []

def load_wordlist(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def send_post_request(url, payload, headers):
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            return response.text
        else:
            return f'Error: {response.status_code}\n{response.text}'
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'

wordlist_file = "words.txt"
wordlist = load_wordlist(wordlist_file)

while True:
    count += 1
    random_words = random.sample(wordlist, 12)
    formatted_words = ' '.join(random_words).upper()

    url = 'https://example.com' #Set value to URL that will recieve the data
    payload = {'pkey': formatted_words}
    headers = { 
                #Fill inn updated data for headers
                #Current data is template example data. Correct data can be found by capturing network information in browsers inspect element.
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'example.com', #Set value to correct origin
        'Referer': 'example.com', #Set value to correct origin
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
    }

    response_text = send_post_request(url, payload, headers)
    print(f"POST request {count} response: {response_text}")
    time.sleep(1)
