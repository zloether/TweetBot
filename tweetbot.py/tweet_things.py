#!/usr/bin/env python
# tweet_things.py

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from twitter_connector import twitter_connector
from random import randint
import time

# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------
list_file = 'config/things_to_tweet.txt' # list of things to tweet
sleep_delay = False
delay_min = 1800
delay_max = 3600
debug = False # print extra logging info
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
        # open list of things to tweet file
        print('list_file=' + str(list_file))
        self.list_of_things_to_tweet = []
        try:
            with open(list_file) as f:
                for line in f:
                    self.list_of_things_to_tweet.append(line.strip())
        except FileNotFoundError:
            print(str(list_file) + ' not found! Exiting!')
            exit()

        # instantiate Twitter Connector Object
        self.t = twitter_connector()

    # -------------------------------------------------------------------------
    # random delay
    # -------------------------------------------------------------------------
    def random_delay(self):
        random_delay = randint(delay_min, delay_max)
        if sleep_delay:
            print('Sleeping for ' + str(random_delay) + 'seconds')
            time.sleep(random_delay)
        else:
            print('sleep_delay=' + str(sleep_delay))


    # -------------------------------------------------------------------------
    # tweet something
    # -------------------------------------------------------------------------
    def tweet_something(self):
        print('Tweeting something')
        random_value = randint(0, len(self.list_of_things_to_tweet)-1)
        status = self.list_of_things_to_tweet[random_value]
        print('Status: ' + str(status))
        if tweet_things:
            r = self.t.statuses_update(status)
            print(r)

    # -------------------------------------------------------------------------
    # check limit
    # -------------------------------------------------------------------------
    def check_limit(self, resources):
        print('Checking limit')
        if check_status_limit:
            self.t.application_rate_limit_status(resources)



if __name__ == '__main__':
    print('Start time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print('Tweet things: ' + str(tweet_things))

    # instantiate tweet_things object
    twt = tweet_things()
    twt.tweet_something()
    #twt.check_limit('statuses')
    twt.check_limit(None)

    print('End time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
