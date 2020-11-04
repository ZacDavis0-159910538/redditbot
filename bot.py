import praw
import prawcore
import random
import datetime
import time
import os
print(os.getcwd())
# FIXME:
# copy your generate_comment functions from the week_07 lab here
#generate_comment
names = ['Joe ', 'Biden ', 'Joe Biden ', 'Former Vice President Joe Biden ', 'Former Vice President ' ,'Former VP ']
name = random.choice(names)
tnames = ['Trump', 'Donald', 'Donald Trump', 'Donald J. Trump' ,'President Trump' ,'President Donald Trump', 'the President']
tname = random.choice(tnames)
concs = ['In conclusion, ' + name + 'is the best choice for your vote in the 2020 presidential election', 'Therefore you are morally obligated to vote for ' +name+ 'this election', 'Thus, you must vote against ' +tname, 'For the sake of our nation, cast your ballot for ' +name]
conc = random.choice(concs)
praises = [' best ',' greatest ',' most amazing ',' better ']
praise = random.choice(praises)
insults = [' worst ', ' most terrible ', ' bad ', ' worse ']
insult = random.choice(insults)
econs = ['institute a $15 federal minimum wage', 'enact Tuition free college for those with household income less than $125,000.00', 'Allow student loans to be relieved in bankruptcy', 'Emergency paid leave for anyone who gets COVID or needs to take care of a loved one']
econ = random.choice(econs)
tecons = [name+'has refused to make his tax returns public, a practice followed by every candidate since 1980. When accused by Clinton at the first debate of not paying federal taxes,' +name+ 'responded, “That makes me smart.” ', name+'exploited a tax loophole to avoid paying taxes on canceled debt, using a maneuver his lawyers advised him against and is now illegal, the Times also reported.', 'According to the Washington Post: https://www.washingtonpost.com/opinions/trump-boasts-about-a-great-economic-record-too-bad-its-obamas/2020/08/31/1eebc59a-ebb8-11ea-b4bc-3a2098fc73d4_story.html "Team Trump, in promulgating the myth of Trump’s economic genius, has recently doubled down on a false narrative: that Trump inherited a recession and magically turned it into a boom. This is almost the exact reverse of events of the past 3½ years. In reality Trump inherited from Obama an expansion — one that, in retrospect, turned out to be the longest in U.S. history — and converted it into a bust."', name+'has engaged in corruption and nepotism ranging from his fake Trump university too using the money from charity to buy himself gifts, including a six-foot painting of himself.']
tecon = random.choice(tecons)
racs = ['Decriminalize cannabis use and expunge convictions', 'Reinstate DACA — allowing new applicants to apply', 'Eliminate mandatory minimum sentences', 'End all incarceration for drug use alone and divert individuals to drug courts and treatment', 'Expand and use the power of the US Justice Department to address systemic misconduct in police departments and prosecutors’ offices']
rac = random.choice(racs)
tracs = ['In 2011,' +name+ 'questioned whether president Obama was born in the US, beginning his years-long obsession with “birtherism.”', 'After the San Bernardino shooting, Trump promised “a total and complete shutdown of Muslims entering the United States.” He later called for more scrutiny of Muslims in the US and surveillance of US mosques.', 'At his campaign kickoff event in June 2015, Trump called Mexicans rapists and criminals. “When Mexico sends its people, they’re not sending their best. They’re not sending you. They’re sending people that have lots of problems, and they’re bringing those problems with us. They’re bringing drugs. They’re bringing crime. They’re rapists,” he said., 8. He claimed Obama was admitted into Columbia and Harvard because of affirmative action.', 'In November, Trump tweeted statistics claiming that 81% of white murder victims are killed by African Americans. According to the FBI, the figure is 15%.']
trac = random.choice(tracs)
dems = ['Restore the voting rights act', 'Ban corporate PAC contributions to candidates, and prohibit lobbyist contributions to those who they lobby' 'ban gerrymandering and voter misinformation strategies such as fake ballot boxes','Introduce a constitutional amendment to entirely eliminate private dollars from our federal elections']
dem = random.choices(dems)
tdems = ['The Trump family has deep business ties to Russia. The Washington Post reported that Trump and his family have made several business trips to the country and rely heavily on Russian investors to buy their real estate properties.  “Russians make up a pretty disproportionate cross-section of a lot of our assets,” Trump’s son, Donald Jr., told a real estate conference in 2008. “We see a lot of money pouring in from Russia.”', 'According to the New York Times "Asked on Wednesday whether he would commit to a “peaceful transfer of power,” President Trump did not say yes. He said: “Well, we’re going to have to see what happens.” He then said we should “get rid of the ballots” — presumably he meant mail-in ballots, but it wasn’t clear — and then ended with these chilling words: “There won’t be a transfer, frankly. There’ll be a continuation.”"', 'According to citizen.org: President Trump has handed control of government to the corporate class. Former Wall Street executives and lobbyists for polluters are driving forward anti-regulatory, corporate-friendly policies that harm ordinary Americans while corporations, foreign governments and Trump businesses profit.','According to the Atlantic: https://www.theatlantic.com/magazine/archive/2020/04/how-to-destroy-a-government/606793/ When Trump came to power, he believed that the regime was his, property he’d rightfully acquired, and that the 2 million civilians working under him, most of them in obscurity, owed him their total loyalty. He harbored a deep suspicion that some of them were plotting in secret to destroy him. He had to bring them to heel before he could be secure in his power. This wouldn’t be easy—the permanent government had defied other leaders and outlasted them. In his inexperience and rashness—the very qualities his supporters loved—he made early mistakes. He placed unreliable or inept commissars in charge of the bureaucracy, and it kept running on its own.' ]
tdem = random.choice(tdems)
edus = [' invest $70 billion in Tribal Colleges and Universities and Minority Serving Institutions.', ' ensure that students with disabilities have access to educational programs and support they need to succeed, from early interventions to post-secondary education.',' support our educators by giving them the pay and dignity they deserve.',' invest in resources for our schools so students grow into physically and emotionally healthy adults, and educators can focus on teaching.',' dramatically increase funding for both public schools and Bureau of Indian Education schools.']
edu = random.choice(edus)
twom = ['In an infamous video from 2005 unearthed by the Washington Post, Trump was heard boasting to Billy Bush, then of Access Hollywood, about the things he could get away with doing to women. As a star, he said, he could, “grab them by the pussy–you can do anything.”','Since the airing of the Access Hollywood tape, at least 12 women have come forward to accuse Trump of sexual assault.','As owner of the Miss Universe pageant, Trump would walk unannounced into dressing rooms where girls as young as 15 were changing. On the Howard Stern Show, he joked about sleeping with the contestants.', 'Trump is accused of raping a 13-year-old girl at billionaire Jeffrey Epstein’s house in 1994. The first court date in her civil suit is scheduled for next month. Trump has denied the allegations.','Trump has spent months attacking Fox News host Megyn Kelly, including the claim that she had been menstruating while moderating a debate. “There was blood coming out of her eyes, blood coming out of her wherever,” he said.']
twom = random.choice(twom)
presx = ['dismissed Sen. John McCain’s war record, which included spending five years as North Vietnamese prisoner of war. “He’s not a war hero,” Trump said. “I like people that weren’t captured.”', 'After Khizr Khan, the father of a soldier killed in Iraq, spoke at the Democratic National Convention and accused Trump of never having sacrificed anything for the country, Trump shot back. He speculated that the Clinton campaign wrote Khan’s speech and that Ghazala Khan, the soldier’s mother, was silent on stage because she wasn’t allowed to speak. “If you look at his wife, she was standing there,” he said. “She had nothing to say… Maybe she wasn’t allowed to have anything to say. You tell me.”','During a fight with Ted Cruz, Trump threatened to “spill the beans” on his wife, Heidi Cruz. Later he tweeted an unflattering photograph of Heidi Cruz alongside his supermodel wife, Melania Trump, with a caption that read “No need to spill the beans, the images are worth a thousand words.”', 'at a rally in South Carolina last November, Trump mocked reporter Serge Kovaleski, who suffers from arthrogryposis, a congenital joint condition that limits movement in his arms. Trump contorted his arms, pretending to impersonate Kovaleski, and said, “Now, the poor guy—you ought to see the guy”. He later said that he would never mock a disabled person because he built wheelchair ramps for his buildings, as is required by law.', 'at the third presidential debate, when Hillary Clinton said that she would raise taxes on wealthy people, including Donald Trump, unless he found a way to get out of paying them, Trump angrily interrupted, calling Clinton a “nasty woman.”', 'encouraged and condoned violence at his rallies, where protesters are routinely punched, beaten and kicked out of the room. “There may be somebody with tomatoes in the audience,” Trump said at a rally in Iowa. “If you see somebody getting ready to throw a tomato, knock the crap out of them, would you? Seriously. Okay?” In one instance, Trump offered to pay the legal fees of a man charged with hitting a protester in the face at his rally. In another, he said he would like to physically attack a protester, saying, “I’d like to punch him in the face, I’ll tell you that.”']
pres = random.choice(presx)
tpersons = ['’s current campaign manager, Steve Bannon, is a former Goldman Sachs banker turned documentary filmmaker, whose movies praised Sarah Palin and Michele Bachman. As chairman of Brietbart News, he insulted and threatened employees while turning the website into a Trump mouthpiece, according to Politico.', 'Reporters covering Trump’s early career would get calls from uncharacteristically helpful and boastful public-relations people called “John Barron” or “John Miller.” Not only did the voice on the phone sound like Trump, it was actually Trump, pretending to be an imaginary spokesperson.', 'tweeted a picture of Hillary Clinton with a Star of David on top of a pile of money, that read “Most Corrupt Candidate Ever!” Even worse, he had retweeted it from the account of a white supremacist. This was not the only time that he has retweeted something from a white supremacist.', 'is friends with the KKK. The Ku Klux Klan endorsed Donald Trump, saying that they thought he would “Make America Great Again.” The endorsement appeared on the front page of their newspaper The Crusader.',"'s frequent and liberal use of the (actual but odd) word “bigly.” Some say he is saying “big league,” but who really knows.",'kicked a crying baby out of a rally, saying, “You can get that baby out of here.”']
tperson = random.choice(tpersons)
def generate_comment_0():
    text = name + 'is the' +praise + 'candidate for the economy because he will' + econ + '. In contrast,' + tname + tecon + conc
    print(text)
    return text

def generate_comment_1():
    text = name + 'is the' +praise+ 'candidate for racism. He will' + rac + tname + trac +conc
    print(text)
    return text

def generate_comment_2():
    text = name + 'is the' +praise+ 'candidate for education. He will' + edu + tname +"'s advisor Betsy Devos is slashing education and making it more expensive and inaccessible for the Average American" +conc
    print(text)
    return text

def generate_comment_3():
    text = tname + 'is the' +insult+ 'presidential candidate.' +tname+ tperson +conc
    print(text)
    return text

def generate_comment_4():
    text = tname + 'is the' +insult+ 'presidential candidate.' +tname+ 'has' +pres +conc
    print(text)
    return text

def generate_comment_5():
    text = tname + 'is the' +insult+ 'candidate for women.' +tname+ 'will' +twom +conc
    print(text)
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    #comments = [generate_comment_0(), generate_comment_1(), generate_comment_2(),generate_comment_3(),generate_comment_4(),generate_comment_5()]
    #comment = random.choice(comments)
    #randomly selected object from a given list of custom class objects https://pynative.com/python-random-choice/
    #objectindex = random.randint(0, len(comments)-1)
    #comment = comments[objectindex]
    num_comment = random.randint(0,5)
    if num_comment == 0:
        return(generate_comment_0())
    if num_comment == 1:
        return(generate_comment_1())
    if num_comment == 2:
        return(generate_comment_2())
    if num_comment == 3:
        return(generate_comment_3())
    if num_comment == 4:
        return(generate_comment_4())
    if num_comment == 5:
        return(generate_comment_5())
    #return (comment)
for i in range(1):
    print('i=',i)
    generate_comment()
# connect to reddit 
reddit = praw.Reddit('bot')
#edit this out later before githubbing



# connect to the debate thread
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jj7fo1/hello_debate_test_hello/'
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jnndas/an_armed_man_is_arrested_outside_a_north_carolina/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

#while True:
for i in range(1000):
#if True:
#while True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print(i)
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    #for c in submission.comments.list():  
        #if type(c) is praw.models.reddit.comment.Comment:
            #print(c.body)

    #for a, b in a_comments_top.items():
        #print ('comments per user=', a,':',b)
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for c in submission.comments.list():
        if type(c) is praw.models.reddit.comment.Comment:
            if str(c.author) == 'jfqt1':
                pass

            else:
                not_my_comments.append(c)
                
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        text = generate_comment() 
        
        try: 
            submission.reply(text)
            print('Task 2 submission success')
        except:
            print('Task 2 exception found')
            print('starting to sleep')
            time.sleep(5)
            print('done sleeping')
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for c in not_my_comments:
            me = False
            for reply in not_my_comments:
                if str(reply.author) == 'jfqt1':
                    me = True
                    #not_my_comments.remove(c)
            #if me == True:
                #not_my_comments.remove(c)
            if me == False:
                comments_without_replies.append(c)
            #else:
                #comments_without_replies.append(c)
        #comments_without_replies.comment_sort = "top"
        print(comments_without_replies)
        #comments_without_replies = sorted(comments_without_replies, key = praw.models.reddit.comment.Comment.score)
        #needs attributes of comments_without_replies, in comments under praw
        #key refers to elements of the list which in this case is comments
    # HINT:
    # this is the most difficult of the tasks,
    # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

    # FIXME (task 4): randomly select a comment from the comments_without_replies list,
    # and reply to that comment
    #
    # HINT:
    # use the generate_comment() function to create the text,
    # and the .reply() function to post it to reddit
    #op = reddit.comment(random.choice(comments_without_replies))
    op = reddit.comment(comments_without_replies)
    text = generate_comment() 
    print('task 4 random reply')
    #from prawcore.exceptions import Forbidden
    if op.is_submitter == True:
        op.reply('Hi op, Thanks for posting this thread.' + text)
    else:
        op.reply(text)
    
    '''
    try: 
        print('task 4 random reply')
        op.reply(text)
    
    except:
        print('task 4 exception found')
        print('starting to sleep')
        time.sleep(5)
        print('done sleeping')
    '''
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    a = random.random()
    topc = []
    if a >= 0.5:
        print('Task 5 Top')
        for c in reddit.subreddit('csci040temp').top(time_filter='month'):
            topc.append(c)
        #rtopc = random.choice(topc)
        submission = random.choice(topc)
        print('submission =', submission)
        t = (submission.title)
        print('title=', t)
        #try: 
            #print('Task 5 submission reply attempt')
            #newsub.reply('I agree '+ t)
            #submission.reply('I agree' + t)
            #print('Task 5 submission reply success')
        #except:
            #print('Task 5 Top exception found')
            #print('starting to sleep')
            #time.sleep(5)
            #print('done sleeping')
    else:
        print('Task 5 Original')
        #text = generate_comment() 
        submission = reddit.submission(url=reddit_debate_url)
        '''
        try:
        except:
            print('Task 5 Original exception found')
            print('starting to sleep')
            time.sleep(5)
            print('done sleeping')
        '''