#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.join(os.path.pardir, 'tweetbot'))))
import tweet_config, twitter_connector
from argparse import ArgumentParser
from unittest import mock


def test_twitter_connector_init():
    # set test config file to use
    #test_config_file = 'tests/test_files/test_config.ini'

    #tc = tweet_config.tweet_config(config_file=test_config_file)
    tc = tweet_config.tweet_config()

    # create tweet_config object
    tconn = twitter_connector.twitter_connector(tweet_config=tc)

    assert isinstance(tconn, twitter_connector.twitter_connector)



@mock.patch('twitter_connector.quote')
def test_percent_encode(mocked_twitter_connector_quote):
    #tc = tweet_config.tweet_config(config_file=test_config_file)
    tc = tweet_config.tweet_config()

    # create tweet_config object
    tconn = twitter_connector.twitter_connector(tweet_config=tc)

    # set test string
    test_input_value = 'this is a test string'

    # call method we want to test
    output = tconn._percent_encode(test_input_value)

    mocked_twitter_connector_quote.assert_called_with(test_input_value, safe="")
    
