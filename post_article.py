#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Post Pocket's artilcle to Slack.

This script post an article which selected from Pocket randomly
to Slack's channel.

This script demands three environment variables.

[POCKET_CONSUMER_KEY]:key to identify Pocket's user
[POCKET_ACCESS_TOKEN]:token to access to Pocket's datas
(https://getpocket.com/developer/docs/authentication)

[SLACK_POST_URL]:Slack's Incoming Webhooks URL
(https://api.slack.com/incoming-webhooks)
"""
import requests
import random
import os
import sys


class NoEnvValExcepion(Exception):
    """Exception Class for invalid environmnet variables."""

    def __init__(self, value):
        """Set exception message."""
        self.value = value

    def __str__(self):
        """Return exception message."""
        return repr(self.value)


def check_defined_env_val():
    """Confirm existence of environment variables."""
    try:
        if os.getenv('POCKET_CONSUMER_KEY') is None or \
           os.getenv('POCKET_ACCESS_TOKEN') is None or \
           os.getenv('SLACK_POST_URL') is None:
            raise NoEnvValExcepion(
                'this script needs to define envirronment variables.'
                )

    except NoEnvValExcepion as e:
        print(e)
        sys.exit(1)


def get_article_from_pocket():
    """Get one dict data from Pocket's articles randomly."""
    consumer_key = os.getenv('POCKET_CONSUMER_KEY')
    access_token = os.getenv('POCKET_ACCESS_TOKEN')
    url = 'https://getpocket.com/v3/get'
    payload = {
        'consumer_key': consumer_key,
        'access_token': access_token,
        'count': 1000,
        'state': 'all',
        'sort': 'newest'
        }
    r = requests.post(url, params=payload)
    responce_data = r.json()

    key, values = random.choice(list(responce_data['list'].items()))
    return values


def post_article_to_slack(article_dict):
    """Post to Slack from argument's infomation."""
    url = os.getenv('SLACK_POST_URL')
    content = {
        'attachments': [
            {
                'title': article_dict['given_title'],
                'title_link': article_dict['given_url'],
                'text': article_dict['excerpt'],
                'pretext': article_dict['given_url'],
                'image_url': article_dict['top_image_url']
            }
        ]
    }
    response_code = requests.post(url, json=content)
    return response_code


if __name__ == '__main__':
    check_defined_env_val()
    article_dict = get_article_from_pocket()
    post_article_to_slack(article_dict)
