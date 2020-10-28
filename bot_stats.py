import praw
#import os
#os.chdir('C:/Users/zac/Dropbox/redditbot')

reddit = praw.Reddit('bot')

submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/')
submission.comments.replace_more(limit=None)
num_del_comments = 0
a_comments_top = {}
for c in submission.comments:
    if type(c) is praw.models.reddit.comment.Comment:
        if c.author is None:
            num_del_comments += 1
            #for reply in comment.replies
        else:
            pass
for c in submission.comments:
    if type(c) is praw.models.reddit.comment.Comment:
        if c.author is None:
            pass
        elif c.author in a_comments_top: 
            a_comments_top[c.author] += 1 
        else:
            a_comments_top[c.author] = 1
print('top comments=', len(submission.comments))
print('deleted comments=', num_del_comments)
for a, b in a_comments_top.items():
    print ('comments per user=', a,':',b)
num_del_comments_total = 0
a_comments_total = {}
    
for c in submission.comments.list():
    if type(c) is praw.models.reddit.comment.Comment:
        if c.author is None:
                num_del_comments_total += 1
        else:
            pass
for c in submission.comments:
    if type(c) is praw.models.reddit.comment.Comment:
        if c.author is None:
            pass
        elif c.author in a_comments_total: 
            a_comments_total[c.author] += 1 
        else:
            a_comments_total[c.author] = 1
print('all comments=', len(submission.comments.list()))
print('deleted comments total=', num_del_comments_total)
for a, b in a_comments_top.items():
    print ('comments per user=', a,':',b)