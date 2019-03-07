cd "%~dp0"
if not exist logs mkdir logs
python.exe tweet_things.py >> logs\tweet_things.log