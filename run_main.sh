#!/bin/sh
cd `dirname ${0}`
mkdir -p logs
python tweetbot.py/tweet_things.py >> logs/tweet_things.log