cd "%~dp0"
if not exist logs mkdir logs
python.exe tweetbot\tweet_things.py >> logs\tweet_things.log