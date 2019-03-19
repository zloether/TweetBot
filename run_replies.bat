cd "%~dp0"
if not exist logs mkdir logs
python.exe tweetbot\tweetreplies.py >> logs\tweet_replies.log
