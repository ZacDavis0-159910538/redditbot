import praw
import random
import datetime
import time
import os
print(os.getcwd())

reddit = praw.Reddit('bot2')
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jl1zec/people_embrace_rebranding_of_proud_boys_to_poor/'
submission = reddit.submission(url=reddit_debate_url)

    #EC Extra submissions
    #Have your bot post new submissions to the /r/csci040 subreddit. These submissions should be from the top submissions of a political subreddit that supports your favorite presidential candidate (e.g. /r/politics or /r/conservative). Your bot must post at least 20 of these submissions to receive the extra credit.
subreddit = reddit.subreddit("politics")
for s in reddit.subreddit("politics").top(limit=40):
    print(s)
    try:
        reddit.subreddit('csci040temp').submit(title=s.title, url=s.url)
    except:
        print('submission exception found')
        print('starting to sleep')
        time.sleep(5)
        print('done sleeping')
