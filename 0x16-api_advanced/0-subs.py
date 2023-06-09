#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import json
from requests import get


def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the number of
    subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Chrome/113.0.0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    result = response.json()

    try:
        return result.get('data').get('subscribers')

    except Exception:
        return 0
