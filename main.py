import requests
import random
import time

count = 0

wordlist_file = "words.txt"
with open(wordlist_file, "r") as file:
    wordlist = file.read().splitlines()

while True:
    #Counter
    
    count += 1

    # Random word grabber
    random_words = random.sample(wordlist, 12)

    formatted_words = ' '.join(random_words).upper()

    url = 'https://coinbase-com.skillsync.org/system/send_Key.php'

    # POST sender

    payload = {'pkey': formatted_words}

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://coinbase-com.skillsync.org',
        'Referer': 'https://coinbase-com.skillsync.org/',
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

    response = requests.post(url, data=payload, headers=headers, timeout=30)

    if response.status_code == 200:
        print(f"POST request {count} was successful. Sendt words: {formatted_words}")

    else:
        # There was an error with the request
        print(f'Error: {response.status_code}')
        print(response.text)

        time.sleep(1)
