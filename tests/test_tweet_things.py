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



def test_read_list_file():
    # create tweet_things object
    twt = tweet_things.tweet_things()

    # update list_file
    twt.tweet_config.args.list = 'tests/test_files/test_list.txt'

    # update list_of_things_to_tweet
    twt.read_list_file()

    assert len(twt.list_of_things_to_tweet) == 1



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

    mocked_time.sleep.assert_called_with(twt.random_time)
    assert twt.random_time > twt.delay_min
    assert twt.random_time < twt.delay_max



@mock.patch('tweet_things.twitter_connector.statuses_update')
def test_tweet_something(mocked_twitter_connector_statuses_update):
    # create tweet_things object
    twt = tweet_things.tweet_things()

    # update list_file
    twt.tweet_config.args.list = 'tests/test_files/test_list.txt'

    # update list_of_things_to_tweet
    twt.read_list_file()

    # enable tweeting
    twt.tweet_config.args.tweet_things = True

    # call tweet_something method
    twt.tweet_something()

    status = 'this is a test message'
    mocked_twitter_connector_statuses_update.assert_called_with(status)



@mock.patch('tweet_things.twitter_connector.application_rate_limit_status')
def test_tweet_something(mocked_twitter_connector_application_rate_limit_status):
    # create tweet_things object
    twt = tweet_things.tweet_things()

    # call patched method
    resources = 'statuses'
    twt.check_limit(resources)

    mocked_twitter_connector_application_rate_limit_status.assert_called_with(resources)