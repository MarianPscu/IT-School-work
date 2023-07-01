import requests
import time


POSTS_URL = "https://jsonplaceholder.typicode.com/"

requests.get(POSTS_URL, timeout = 30)


def get_with_retry(url):

    try:

        resp = requests.get(POSTS_URL, timeout= (3.5, 30))

    except requests.ConnectTimeout as err:

        print("Connection timed out. Retrying after 3 seconds")
        time.sleep(3)
        get_with_retry(url)


    else:
        print(resp)



get_with_retry(POSTS_URL)