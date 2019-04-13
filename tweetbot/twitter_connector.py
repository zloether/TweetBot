#!/usr/bin/env python
# twitter_connector.py
# https://requests-oauthlib.readthedocs.io/en/latest/oauth1_workflow.html

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from requests_oauthlib import OAuth1Session
from requests import Request
from urllib.parse import quote
from tweet_config import tweet_config
import datetime
import time

# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------
sleep_delay = 60

# -----------------------------------------------------------------------------
# twitter_connector
# -----------------------------------------------------------------------------
class twitter_connector():
    def __init__ (self, tweet_config):
        self.tweet_config = tweet_config
        api_cred = self.tweet_config.get_api_creds()
        self.twitter = OAuth1Session(client_key=api_cred[0], \
                                    client_secret=api_cred[1], \
                                    resource_owner_key=api_cred[2], \
                                    resource_owner_secret=api_cred[3])
        self.request_counter = []
        self.sleep_delay = sleep_delay
        self.last_call = None

    # percent encode input string for web requests
    def _percent_encode(self, input_val):
        return quote(str(input_val), safe='')

    def _eval_request_counter(self):
        time_window = datetime.timedelta(minutes=-15)
        for i in self.request_counter:
            if i < time_window:
                self.request_counter.remove(i)

        if len(self.request_counter) <= 15:
            now = datetime.datetime.now()
            self.request_counter.append(now)
            return True
        else:
            delay = self.request_counter[0] - time_window
            time.sleep(delay)

    def application_rate_limit_status(self, resource_item=None):
        url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
        if resource_item:
            if self.last_call:
                resources = self.last_call.split('/')[1].split('\\')[0]
        else:
            resources = None
        payload = {'resources': resources}
        r = self.twitter.get(url, params=payload)
        self._parse_response(r)
        j = r.json()
        reset_times = set()
        if resources:
            limit = j['resources'][resources][resource_item]['limit']
            remaining = j['resources'][resources][resource_item]['remaining']
            reset = j['resources'][resources][resource_item]['reset']
            if int(remaining) < 6:
                unix_time = int(time.time())
                delay_time = int(reset) - unix_time
                reset_times.add(delay_time)
                print('Resource: ' + i + ', Limit: ' + limit + ', Remaining: ' + remaining + ', Delay: ' + delay_time + ' seconds')
        else:
            for i in j['resources']:
                if self.tweet_config.get_verbose():
                    print(i)
                for n in j['resources'][i]:
                    if self.tweet_config.get_verbose():
                        print(n)
                    limit = j['resources'][i][n]['limit']
                    remaining = j['resources'][i][n]['remaining']
                    reset = j['resources'][i][n]['reset']
                    if int(remaining) < 6:
                        unix_time = int(time.time())
                        delay_time = int(reset) - unix_time
                        reset_times.add(delay_time)
                        print('Resource: ' + str(n) + ', Limit: ' + str(limit) + ', Remaining: ' + str(remaining) + ', Delay: ' + str(delay_time) + ' seconds')

    def _parse_response(self, response):
        if response.status_code == 200:
            return response.text
        elif response.status_code == 429:
            print('Rate limit exceeded, sleeping for ' + str(sleep_delay) + ' seconds')
            time.sleep(self.sleep_delay) # sleep for specified amount of time
            r = self.twitter.send(response.request) # resend last request
            return self._parse_response(r)
        else:
            print('Code: ' + response.text)
            print(response.status_code)

    def statuses_update(self, status):
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        payload = {'status': status}
        self.last_call = None
        r = self.twitter.post(url, data=payload)
        return self._parse_response(r)

    def statuses_reply(self, status, in_reply_to_status_id):
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        payload = {'status': status, 'in_reply_to_status_id': in_reply_to_status_id, 'auto_populate_reply_metadata': 'true'}
        self.last_call = None
        r = self.twitter.post(url, data=payload)
        return self._parse_response(r)

    def statuses_home_timeline(self):
        url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
        self.last_call = '''\\/statuses\\/home_timeline'''
        r = self.twitter.get(url)
        return self._parse_response(r)

    def statuses_mentions_timeline(self, max_id=None, since_id=None, count=None):
        url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
        payload = {'include_entities': 'false', 'max_id': max_id, 'since_id': since_id, 'count': count}
        self.last_call = '''\\/statuses\\/mentions_timeline'''
        r = self.twitter.get(url, params=payload)
        return self._parse_response(r)

    def followers_ids(self):
        url = 'https://api.twitter.com/1.1/followers/ids.json'
        self.last_call = '''\\/followers\\/ids'''
        r = self.twitter.get(url)
        return self._parse_response(r)

    def users_lookup(self, user_id_list):
        url = 'https://api.twitter.com/1.1/users/lookup.json'
        user_ids = ''
        for item in user_id_list:
            user_ids += str(item) + ','
        payload = {'user_id': user_ids}
        self.last_call = '''\\/users\\/lookup'''
        r = self.twitter.get(url, params=payload)
        return self._parse_response(r)

    def friends_ids(self, cursor=None):
        url = 'https://api.twitter.com/1.1/friends/ids.json'
        payload = {'cursor': cursor}
        self.last_call = '''\\/friends\\/ids'''
        r = self.twitter.get(url, params=payload)
        return self._parse_response(r)

    def friendships_create(self, user_id):
        url = 'https://api.twitter.com/1.1/friendships/create.json'
        payload = {'user_id': user_id}
        self.last_call = None
        r = self.twitter.post(url, data=payload)
        return self._parse_response(r)





if __name__ == '__main__':
    #from sys import argv
    #try:
    #    script, status = argv
    #except:
    #    print('Usage: This script takes status as an argument.')
    #    exit()

    t = twitter_connector()
    t.statuses_home_timeline()
    #t.statuses_update(status)
