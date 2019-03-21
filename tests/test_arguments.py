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
    test_config_file = 'tests/test_files/test_config.ini'
    
    # try --config argument
    tc.args = tc.parser.parse_args(['--config', test_config_file])
    
    assert tc.args.config == test_config_file



def test_argument_list():
    # create tweet_config object
    tc = tweet_config.tweet_config()

    # test list file to use
    test_list_file = 'test/test_files/test_list.txt'

    # try --list argument
    tc.args = tc.parser.parse_args(['--list', test_list_file])
    
    assert tc.args.list == test_list_file


