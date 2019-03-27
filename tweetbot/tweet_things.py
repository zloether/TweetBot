#!/usr/bin/env python
# tweet_things.py

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from twitter_connector import twitter_connector
from tweet_config import tweet_config
from random import randint
import time

# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------

tweet_things = False # False for testing, True to actually tweet things
check_status_limit = True

follow_new_users = False # for future use
update_requested_list = True # for future use
check_already_requested = True # for future use


# -----------------------------------------------------------------------------
# tweet things
# -----------------------------------------------------------------------------
class tweet_things(object):
    def __init__(self):
        self.sleep_delay = False
        self.delay_min = 1800
        self.delay_max = 3600

        # set up tweet_config object
        self.tweet_config = tweet_config()

        # instantiate Twitter Connector Object
        self.tc = twitter_connector(self.tweet_config)


    # -------------------------------------------------------------------------
    # random delay
    # -------------------------------------------------------------------------
    def read_list_file(self):
        list_file = self.tweet_config.get_list_file()
        print('list_file: ' + str(list_file))

        list_of_things_to_tweet = []
        try:
            with open(list_file) as f:
                for line in f:
                    list_of_things_to_tweet.append(line.strip())
        except FileNotFoundError:
            print(str(list_file) + ' not found! Exiting!')
            exit()
        
        if len(list_of_things_to_tweet) > 0:
            self.list_of_things_to_tweet = list_of_things_to_tweet
        else:
            print('Error: List of things to tweet is empty.')
            print('List file: ' + str(list_file))
            print('Exiting!')
            exit()


    # -------------------------------------------------------------------------
    # random delay
    # -------------------------------------------------------------------------
    def random_delay(self):
        self. random_time = randint(self.delay_min, self.delay_max)
        if self.sleep_delay:
            print('Sleeping for ' + str(self.random_time) + 'seconds')
            time.sleep(self.random_time)
        else:
            print('sleep_delay=' + str(self.random_time))


    # -------------------------------------------------------------------------
    # tweet something
    # -------------------------------------------------------------------------
    def tweet_something(self):
        print('Tweeting something')
        random_value = randint(0, len(self.list_of_things_to_tweet)-1)
            
        status = self.list_of_things_to_tweet[random_value]
        print('Status: ' + str(status))
        if self.tweet_config.get_tweet_things():
            r = self.tc.statuses_update(status)
            print(r)

    # -------------------------------------------------------------------------
    # check limit
    # -------------------------------------------------------------------------
    def check_limit(self, resources):
        print('Checking limit')
        if check_status_limit:
            self.tc.application_rate_limit_status(resources)



if __name__ == '__main__':
    print('Start time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    #print('Tweet things: ' + str(tweet_things))

    # instantiate tweet_things object
    twt = tweet_things()
    twt.tweet_something()
    #twt.check_limit('statuses')
    twt.check_limit(None)

    print('End time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
