#!/bin/sh
cd `dirname ${0}`
mkdir -p logs
python tweetbot/tweet_replies.py >> logs/tweet_replies.log