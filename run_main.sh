#!/bin/sh
cd `dirname ${0}`
mkdir -p logs
python tweetbot/tweet_things.py >> logs/tweet_things.log