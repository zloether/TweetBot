#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join(os.path.pardir, 'tweetbot'))))
import tweet_things



def test_tweet_things_init():
    # create tweet_things object
    twt = tweet_things.tweet_things()

    assert isinstance(twt, tweet_things.tweet_things)
