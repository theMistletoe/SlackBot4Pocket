# SlackBot4Pocket
====

Script for posting Pocket( https://getpocket.com )'s articles to Slack( https://slack.com ).

## Description
This script posts an article selected randomly from Pocket to Slack.

## Requirement
- python
- below environment variables
 - [POCKET_CONSUMER_KEY]:key to identify Pocket's user
 - [POCKET_ACCESS_TOKEN]:token to access to Pocket's datas
 (https://getpocket.com/developer/docs/authentication)
 - [SLACK_POST_URL]:Slack's Incoming Webhooks URL
 (https://api.slack.com/incoming-webhooks)

## Usage

`python ./post_article.py`

## Licence

[MIT](https://github.com/theMistletoe/SlackBot4Pocket/blob/master/LICENSE)

## Author

[theMistletoe](https://github.com/theMistletoe)
