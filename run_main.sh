#!/bin/sh
cd `dirname ${0}`
mkdir -p logs
python tweet_things.py >> logs/tweet_things.log