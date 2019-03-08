#!/usr/bin/env python
# tweet_config.py


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
import configparser
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
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
    
    def get_api_creds(self):
        oauth_consumer_key = self.config['API_KEYS']['oauth_consumer_key']
        oauth_consumer_secret = self.config['API_KEYS']['oauth_consumer_secret']
        oauth_token = self.config['API_KEYS']['oauth_token']
        oauth_token_secret = self.config['API_KEYS']['oauth_token_secret']
        print(oauth_consumer_key, oauth_consumer_secret, oauth_token, oauth_token_secret)



if __name__ == '__main__':
    tc = tweet_config()
    tc.get_api_creds()