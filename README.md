# tweetbot.py
![GitHub](https://img.shields.io/github/license/zloether/tweetbot.py.svg)
![Python](https://img.shields.io/badge/python-v3.5+-blue.svg)

A Twitter bot written in Python

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#Usage)
	- [Windows](#windows)
	- [Linux](Linux)
- [Logging](#logging)
- [Status Files](#status-files)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed in order to run `tweetbot.py`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `tweetbot.py` has not been tested with Python 2 and will probably not work without changing some things.*

After Python is installed, install the *requests* and *requests_oauthlib* libraries.
```
pip install requests requests_oauthlib
```

## Installation
Download the latest version from GitHub using Git.
```
git clone https://github.com/zloether/tweetbot.py.git
```
This will create a directory called *tweetbot.py* and all the code will be in it.

## Configuration
You need a Twitter developer account in order to connect to the API. Get started [here](https://developer.twitter.com/en.html).

Edit the `tweetthings_config.py` file and insert your API credentials for these values:

- *oauth_consumer_key*
- *oauth_consumer_secret*
- *oauth_token*
- *oauth_token_secret*


The `things_to_tweet.txt` files contains a newline seperated list of  things to tweet. Whenever `tweetthings.py` runs, it will read this file. When its time to tweet something, it will pick a line at random from this file and tweet that line.



Three scripts use boolean values to control if they write to the API. Toggle them between `True` and `False` to enable or disable, respectively, writing to the API.
- `tweet_things.py`
- `tweet_replies.py`
- `twitter_followers.py`

## Usage
### **_Windows_**

The `run_main.bat` script will call the `tweet_things.py` script and store output to the log file.

The `run_replies.bat` script will call the `tweet_replies.py` script and store output to the log file.


### **_Linux_**

The `run_main.sh` script will call the `tweet_things.py` script and store output to the log file.

The `run_replies.sh` script will call the `tweet_replies.py` script and store output to the log file.


## Logging
A `logs` directory will be generated inside the project directory.

The `tweet_things.py` script will write logs to `logs/tweet_things.log`.

The `tweet_replies.py` script will write logs to `logs/tweet_replies.log`.

## Status Files
Several status files will get automatically generated in the project directory when `tweetthings.py` runs:
- `anchor.txt`- Status ID for the last seen reply message
- `requested_friends.txt` - ID for users that have already been requested to be friends

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Requests: HTTP for Humans](http://python-requests.org/)
* [Requests-OAuthlib: OAuth for Humans](https://requests-oauthlib.readthedocs.io/)

