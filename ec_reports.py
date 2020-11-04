import praw
import random
import datetime
import time
import os
print(os.getcwd())

reddit = praw.Reddit('bot2')
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jl1zec/people_embrace_rebranding_of_proud_boys_to_poor/'
submission = reddit.submission(url=reddit_debate_url)
subreddit = reddit.subreddit('csci040temp')

#EC reports submissions and comments
comment = reddit.comment in submission.comments.list()
reported_comments = []
reported_submissions = []
'''
make new python file
add try and excepts, add time sleep
print('Task 2 exception found')
    print('starting to sleep')
    time.sleep(5)
    print('done sleeping')
'''
for i in range(1):
    for s in subreddit.new(limit=10):
        #if type(s) is praw.models.reddit.submission:
            if 'Donald' or 'Trump' or 'President' in str(s.title) and not 'Vice President' or 'Biden' or 'Joe':
                if s not in reported_submissions:
                    try:
                        s.report("This bot submission shares fake news")
                        reported_submissions.append(s)
                        print('submission report success')
                        print(reported_submissions)
                    except:
                        print('submission report exception found')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')

    for c in submission.comments.list():
        if type(c) is praw.models.reddit.comment.Comment:
            if 'Donald' or 'Trump' or 'President' in str(s.title) and not 'Vice President' or 'Biden' or 'Joe' in str(c.body):
                if c not in reported_comments:
                    try:
                        c.report("This bot shares fake pro-Trump propaganda")
                        reported_comments.append(c)
                        print('comment sucess')
                    except:
                        print('comment exception found')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')
    
