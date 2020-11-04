
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

#EC downvotes submissions and comments
comment = reddit.comment in submission.comments.list()
downvoted_comments = []
downvoted_submissions = []
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
            if 'Donald' or 'Trump' or 'President' in str(s.title) and not 'Vice President':
                if s not in downvoted_submissions:
                    try:
                        s.downvote()
                        downvoted_submissions.append(s)
                        print('submission downvote success')
                        print(downvoted_submissions)
                    except:
                        print('submission downvote exception found')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')
    
    for c in submission.comments.list():
        if type(c) is praw.models.reddit.comment.Comment:
            if 'Donald' or 'Trump' or 'President' in str(s.title) and not 'Vice President' in str(c.body):
                if c not in downvoted_comments:
                    try:
                        c.downvote()
                        downvoted_comments.append(c)
                        print('comment sucess')
                    except:
                        print('comment exception found')
                        print('starting to sleep')
                        time.sleep(5)
                        print('done sleeping')
    
