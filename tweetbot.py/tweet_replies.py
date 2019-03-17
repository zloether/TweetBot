#!/usr/bin/env python
# tweet_replies.py

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from twitter_connector import twitter_connector
from twitter_followers import twitter_followers
from tweet_config import tweet_config
from random import randint
import json
import time


# -----------------------------------------------------------------------------
# settings
# -----------------------------------------------------------------------------
send_replies = False # False for testing, True to actually tweet replies
count = None # get default number of tweets per connection
list_file = 'config/things_to_tweet.txt'
anchor_file = 'config/anchor.txt'
update_friends = True # check for new followers and add them as friends

def tweet_replies(twitter_connector):
    print('anchor_file=' + str(anchor_file))

    # -------------------------------------------------------------------------
    # set up tweet_config object
    # -------------------------------------------------------------------------
    twitter_config = tweet_config()


    # -------------------------------------------------------------------------
    # open the things to tweet file
    # -------------------------------------------------------------------------
    list_file = twitter_config.get_list_file()
    print('list_file: ' + str(list_file))
    list_of_things_to_tweet = []
    try:
        with open(list_file) as f:
            for line in f:
                list_of_things_to_tweet.append(line.strip())
    except FileNotFoundError:
        print(str(list_file) + ' not found! Exiting!')
        exit()

    # -------------------------------------------------------------------------
    # open the anchor file
    # -------------------------------------------------------------------------
    since_id = None
    try:
        with open(anchor_file) as f:
            line = f.readline().strip()
            if line:
                since_id = line
    except FileNotFoundError:
        print('Anchor file not found: ' + anchor_file)
    print("since_id: " + str(since_id))

    # -------------------------------------------------------------------------
    # create Twitter connector object
    # -------------------------------------------------------------------------
    t = twitter_connector #********************************************************* variable passed into this function is getting renamed. FIX THIS!!

    # -------------------------------------------------------------------------
    # check for new followers and add them as friends
    # -------------------------------------------------------------------------
    if update_friends:
        twitter_followers(t)

    # -------------------------------------------------------------------------
    # get recent replies
    # -------------------------------------------------------------------------
    max_id = None
    new_since_id = False
    get_replies = True
    while get_replies:
        r = t.statuses_mentions_timeline(max_id=max_id, since_id=since_id, count=count)
        print(r)
        if r != '[]': # if there are new replies
            tweet_ids = {} # dict of replies
            j = json.loads(r)
            for i in j:
                # parse out tweet ID and screen name
                tweet_ids[int(i['id_str'])] = i['user']['screen_name']
            print('Tweet IDs: ' + str(tweet_ids))

            # -----------------------------------------------------------------
            # respond to recent replies
            # -----------------------------------------------------------------
            print('Starting replies')
            for tweet_id in tweet_ids:
                random_value = randint(0, len(list_of_things_to_tweet)-1)
                screen_name = str(tweet_ids[tweet_id])
                status = '@' + screen_name + ' ' + list_of_things_to_tweet[random_value]
                print('\tRandom value: ' + str(random_value) + '; ' +\
                        'Tweet ID: ' + str(tweet_id) + '; ' +\
                        'Screen name: ' + screen_name + '; ' +\
                        'Status: ' + str(status))
                if send_replies:
                    r = t.statuses_reply(status, tweet_id)
                    print(r)
                else:
                    print('Not tweeted')

            max_id = min(tweet_ids) - 1
            if not new_since_id: # first time getting replies only
                new_since_id = max(tweet_ids) # used to update anchor file
        else: # if there aren't new replies
            get_replies = False

    # -------------------------------------------------------------------------
    # update anchor file with the most recent since_id
    # -------------------------------------------------------------------------
    if new_since_id:
        print('Updating anchor file')
        with open(anchor_file, 'w') as f:
            f.write(str(new_since_id))
    else:
        print('No new since_id')


if __name__ == '__main__':
    print('Start time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print('Tweet replies: ' + str(send_replies))

    # set up tweet_config object
    twitter_config = tweet_config()

    # create Twitter connector object
    t = twitter_connector(twitter_config)
    tweet_replies(t)

    print('End time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
