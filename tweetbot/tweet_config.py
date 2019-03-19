#!/usr/bin/env python
# tweet_config.py


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
import configparser
import argparse
from os import path



# -----------------------------------------------------------------------------
# settings
# -----------------------------------------------------------------------------
app_path = path.split(path.split(path.realpath(__file__))[0])[0]
config_file = app_path + '/config/tweet_config.ini'



# -----------------------------------------------------------------------------
# set up tweet_config class
# -----------------------------------------------------------------------------
class tweet_config():
    def __init__(self, config_file=config_file):
        # parse arguments
        self.parse_arguments()
        
        # set up config parser
        self.config = configparser.ConfigParser()
        
        # give priority to config file passed as arugment
        if self.args.config:
            self.config.read(self.args.config)
        else:
            self.config.read(config_file)


    
    def parse_arguments(self):
        # create parser object
        self.parser = argparse.ArgumentParser(description='A Twitter bot')

        # setup arugment for specifying a config file to use
        self.parser.add_argument('-c', '--config', dest='config', metavar='file',
                            action='store', help='specify config file to use')
        
        # setup arugment for specifying a list of things to tweet
        self.parser.add_argument('-l', '--list', dest='list', metavar='file',
                            action='store', help='specify list of things to tweet')
        
        # parse the arguments
        self.args = self.parser.parse_args()

        
    
    def get_api_creds(self):
        oauth_consumer_key = self.config['API_KEYS']['oauth_consumer_key']
        oauth_consumer_secret = self.config['API_KEYS']['oauth_consumer_secret']
        oauth_token = self.config['API_KEYS']['oauth_token']
        oauth_token_secret = self.config['API_KEYS']['oauth_token_secret']
        return oauth_consumer_key, oauth_consumer_secret, oauth_token, oauth_token_secret
    


    def get_list_file(self):
        list_file = self.config['LIST']['list']
        return list_file




if __name__ == '__main__':
    tc = tweet_config()
    tc.get_api_creds()