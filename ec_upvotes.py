
import praw
import random
import datetime
import time
import os
print(os.getcwd())

reddit = praw.Reddit('bot1')
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jl1zec/people_embrace_rebranding_of_proud_boys_to_poor/'
submission = reddit.submission(url=reddit_debate_url)
subreddit = reddit.subreddit('csci040temp')

#EC upvotes submissions and comments
comment = reddit.comment in submission.comments.list()

'''
make new python file
add try and excepts, add time sleep
print('Task 2 exception found')
    print('starting to sleep')
    time.sleep(5)
    print('done sleeping')
'''
a = 0
for i in range(30):
    a += 1
    upvoted_comments = []
    upvoted_submissions = []
    print('bot'+str(a)+'starting up')
    reddit = praw.Reddit('bot'+str(a))
    time.sleep(5)
    for s in subreddit.new(limit=10):
        #if type(s) is praw.models.reddit.submission:
            if 'Joe' or 'Biden' or 'VP' or 'Vice President' in str(s.title):
                if s not in upvoted_submissions:
                    try:
                        s.upvote()
                        upvoted_submissions.append(s)
                        print('submission upvote success')
                        print(upvoted_submissions)
                    except:
                        print('submission upvote exception found/already upvoted by this bot')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')
    commlist = submission.comments.list()
    for c in commlist[0:10]:
        if type(c) is praw.models.reddit.comment.Comment:
            if 'Joe' or 'Biden' or 'VP' or 'Vice President' in str(c.body):
                if c not in upvoted_comments:
                    try:
                        c.upvote()
                        upvoted_comments.append(c)
                        print('comment sucess')
                    except:
                        print('comment exception found')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')
    
