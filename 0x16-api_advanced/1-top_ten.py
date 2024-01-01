#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get('{}/r/{}/.json?sort={}&limit={}'.format(
        url, subreddit, 'top', 10),
        headers=header,
        allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
