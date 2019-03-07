cd "%~dp0"
if not exist logs mkdir logs
python.exe tweetbot.py\tweet_things.py >> logs\tweet_things.log