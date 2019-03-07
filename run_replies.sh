#!/bin/sh
cd `dirname ${0}`
mkdir -p logs
python tweet_replies.py >> logs/tweet_replies.log