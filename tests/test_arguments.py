#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from tweetbot import tweet_config
from argparse import ArgumentParser



def test_parse_arguments():
    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'
    
    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    assert isinstance(tc.parser, ArgumentParser)



def test_get_help(capsys):
    # create tweet_config object
    tc = tweet_config.tweet_config()
    
    # print help
    tc.parser.print_help()

    # capture stdout
    out = capsys.readouterr()[0]

    assert out.startswith('usage: ')



def test_argument_config():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    # set test config file to use
    test_config_file = 'test_files/test_config.ini'
    
    # try --config argument
    tc.args = tc.parser.parse_args(['--config', test_config_file])
    
    assert tc.args.config == test_config_file



def test_get_api_creds():
    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    # call method
    oauth_consumer_key, oauth_consumer_secret, oauth_token, oauth_token_secret = tc.get_api_creds()

    assert oauth_consumer_key == 'test_oauth_consumer_key'
    assert oauth_consumer_secret == 'test_oauth_consumer_secret'
    assert oauth_token == 'test_oauth_token'
    assert oauth_token_secret == 'test_oauth_token_secret'



def test_argument_list():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    # test list file to use
    test_list_file = 'test_files/test_list.txt'

    # try --list argument
    tc.args = tc.parser.parse_args(['--list', test_list_file])
    
    assert tc.args.list == test_list_file



def test_status_check():
    # set default config file to use
    test_config_file = 'config/tweet_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    assert tc.get_status_check() == True

    # try --status-disable argument
    tc.args = tc.parser.parse_args(['--status-disable'])
    assert tc.get_status_check() == False

    # try --status-enable argument
    tc.args = tc.parser.parse_args(['--status-enable'])
    assert tc.get_status_check() == True



def test_argument_tweet_things():
    # create tweet_config object
    tc = tweet_config.tweet_config()
    assert tc.get_tweet_things() == False
    
    # set test config file to use
    test_config_file = 'tests/test_files/test_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)
    assert tc.get_tweet_things() == True

    # try --tweet-disable argument
    tc.args = tc.parser.parse_args(['--tweet-disable'])
    assert tc.get_tweet_things() == False
    
    # try --tweet-enable argument
    tc.args = tc.parser.parse_args(['--tweet-enable'])
    assert tc.get_tweet_things() == True



def test_argument_verbose():
    # set default config file to use
    test_config_file = 'config/tweet_config.ini'

    # create tweet_config object
    tc = tweet_config.tweet_config(config_file=test_config_file)

    assert tc.get_verbose() == False

    # try --verbose argument
    tc.args = tc.parser.parse_args(['--verbose'])
    
    assert tc.get_verbose() == True