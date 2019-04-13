#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from tweetbot import tweet_config
from argparse import ArgumentParser


def test_tweet_config_init():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    assert isinstance(tc, tweet_config.tweet_config)



def test_get_api_creds():
    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    # get api creds
    creds = tc.get_api_creds()
    
    assert creds[0] == 'test_oauth_consumer_key'
    assert creds[1] == 'test_oauth_consumer_secret'
    assert creds[2] == 'test_oauth_token'
    assert creds[3] == 'test_oauth_token_secret'



def test_get_list_file():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    # test list file to check against
    default_list_file = 'config/things_to_tweet.txt'

    # test default list file
    assert tc.get_list_file() == default_list_file

    # test list file to use
    test_list_file = 'test/test_files/test_list.txt'

    # try --list argument
    tc.args = tc.parser.parse_args(['--list', test_list_file])

    assert tc.get_list_file() == test_list_file


    