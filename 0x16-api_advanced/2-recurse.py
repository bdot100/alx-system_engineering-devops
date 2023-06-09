#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function should return None.
"""
from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """
    recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given
    subreddit.
    """
    global after
    if not subreddit:
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {
        #"limit": 100,
        "after": after,
        "raw_json": 1
    }
    headers = {
        "User-Agent": "python-requests/2.31.0"
    }

    response = get(url, params=params, headers=headers, allow_redirects=False)

    return response.status_code
    
    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = response.json().get("data").get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return None



print(recurse('programming', hot_list=[]))