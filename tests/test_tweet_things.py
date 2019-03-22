#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join(os.path.pardir, 'tweetbot'))))
import tweet_things
from unittest import mock


def test_tweet_things_init():
    # create tweet_things object
    twt = tweet_things.tweet_things()

    assert isinstance(twt, tweet_things.tweet_things)



@mock.patch('tweet_things.time')
def test_random_delay(mocked_time):
    # create tweet_things object
    twt = tweet_things.tweet_things()

    # make sure sleep_delay is enabled
    print(twt.sleep_delay)
    twt.sleep_delay = True
    print(twt.sleep_delay)

    # call random_delay
    twt.random_delay()

    mocked_time.sleep.assert_called_once()

