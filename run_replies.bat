cd "%~dp0"
if not exist logs mkdir logs
python.exe tweetreplies.py >> logs\tweet_replies.log
