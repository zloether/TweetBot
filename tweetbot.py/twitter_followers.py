#!/usr/bin/env python
# twitter_followers.py

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from twitter_connector import twitter_connector
import json
import time

def twitter_followers(twitter_connector):
    # -------------------------------------------------------------------------
    # settings
    # -------------------------------------------------------------------------
    follow_new_users = False # False for testing, True to actually follow people
    debug = True # prints extra logging info
    requested_list = 'requested_friends.txt'
    update_requested_list = True
    check_already_requested = True

    # -------------------------------------------------------------------------
    # get user IDs we've already requested to follow
    # -------------------------------------------------------------------------
    if check_already_requested:
        already_requested = set()
        try:
            with open(requested_list, 'r') as f:
                line = f.readline()
                while line:
                    already_requested.add(int(line.strip()))
                    line = f.readline()
        except FileNotFoundError:
            pass

        print('Already requested: ' + str(already_requested))

    # -------------------------------------------------------------------------
    # Twitter connector
    # -------------------------------------------------------------------------
    t = twitter_connector

    # -------------------------------------------------------------------------
    # get followers
    # -------------------------------------------------------------------------
    r = t.followers_ids()
    j = json.loads(r)
    follower_ids = set(j['ids'])
    if debug:
        print('Follower IDs: ' + str(follower_ids))

    # -------------------------------------------------------------------------
    # get friends (users I follow)
    # -------------------------------------------------------------------------
    r = t.friends_ids()
    j = json.loads(r)
    friends_ids = set(j['ids'])
    if debug:
        print('Friends IDs: ' + str(friends_ids))

    # -------------------------------------------------------------------------
    # get user IDs following me who I am not following
    # -------------------------------------------------------------------------
    not_following = follower_ids - friends_ids
    if check_already_requested:
        not_following = not_following - already_requested
    print('Not following IDs: ' + str(not_following))

    # -------------------------------------------------------------------------
    # follow users I'm not currently following
    # -------------------------------------------------------------------------
    if follow_new_users:
        for user_id in not_following:
            r = t.friendships_create(user_id)
            if debug:
                print(r)

    # -------------------------------------------------------------------------
    # update list of already requested user IDs
    # -------------------------------------------------------------------------
    if check_already_requested and update_requested_list and follow_new_users:
        with open(requested_list, 'a') as f:
            for user_id in not_following:
                f.write(str(user_id) + '\n')


if __name__ == '__main__':
    print('Start time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))

    # create Twitter connector object
    t = twitter_connector()
    twitter_followers(t)

    print('End time: ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print()
