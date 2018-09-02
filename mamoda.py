"""
creator : orangmiliter

"""
import tweepy
from tkinter import *
import datetime, time, sys
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt
from keys import keys
#ukuran
ormil = ('times', 20, 'bold')
labelMU  =('bold')

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
# print(user.name)
# print(user.location)
print("Welcome\t\t: " + user.name)
print("Your location\t: " + user.location)
print("=====================================")


root = Tk()
root.configure(background='#0084B4')
root.geometry("300x480")
root.title("OrangMiliter")
frame = Frame(root)

widget = Label(root, text="MaMo'da", background='#0084B4', fg='white', font=ormil)

label1 = Label( root, text="cari", background='#0084B4', fg='white', font=labelMU)
E1 = Entry(root, bd =2)

label2 = Label( root, text="Jumlah Tweet", background='#0084B4', fg='white', font=labelMU)
E2 = Entry(root, bd =2)

label3 = Label( root, text="Respon", background='#0084B4', fg='white', font=labelMU)
E3 = Entry(root, bd =2)

label4 = Label( root, text="balas", background='#0084B4', fg='white', font=labelMU)
E4 = Entry(root, bd =2)

label5 = Label( root, text="Retweet", background='#0084B4', fg='white', font=labelMU)
E5 = Entry(root, bd =2)

label6 = Label( root, text="Sukai", background='#0084B4', fg='white', font=labelMU)
E6 = Entry(root, bd =2)
label7 = Label( root, text="Ikuti", background='#0084B4', fg='white', font=labelMU)
E7 = Entry(root, bd =2)
label8 = Label( root, text="Lihat Info", background='#0084B4', fg='white', font=labelMU)
E8 = Entry(root, bd =2)
label9 = Label(root, text="sentiment analysis", background='#0084B4', fg='white', font=labelMU)
E9 = Entry(root, bd =2)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()
def getE8():
    return E8.get()
def getE9():
    return E9.get()


def mainFunction():
    getE1()
    search = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)

    getE3()
    phrase = getE3()

    getE4()
    reply = getE4()

    getE5()
    retweet = getE5()

    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    getE8()
    location = getE8()

    getE9()
    sensitiv = getE9()

    polarity_list = []
    numbers_list = []
    number = 1

    if reply == "ya":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


    if retweet == "ya":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted tweet @' + tweet.user.screen_name)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "ya":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited tweet @' + tweet.user.screen_name)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "ya":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed @' + tweet.user.screen_name)
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if location == "ya":
        for tweet in tweepy.Cursor(api.search, search, tweet_mode='extended').items(numberOfTweets):
            try:
                api.get_user(tweet.user.screen_name)
                print("create\t\t:" + str(tweet.created_at))
                print("Name\t\t: " + tweet.user.name)
                print("username\t: @" + tweet.user.screen_name)
		#print(tweet.user.screen_name)
                print("Location\t: " + tweet.user.location)
                print("Following\t: " + str(tweet.user.friends_count))
                print("Followers\t: " + str(tweet.user.followers_count))
                print("Status\t\t: " + tweet.full_text)
                print("==========Pembatas==========")
                #time.sleep(3)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if sensitiv == "ya":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                analysis = TextBlob(tweet.text)
                analysis = analysis.sentiment
                polarity = analysis.polarity
                polarity_list.append(polarity)
                numbers_list.append(number)
                number = number + 1

            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

        #plot
        axes = plt.gca()
        axes.set_ylim([-1, 2])

        plt.scatter(numbers_list, polarity_list)

        averagePolarity = (sum(polarity_list))/(len(polarity_list))
        averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
        time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")
        plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))
        plt.title("Sentiment of " + search + " on Twitter")
        plt.xlabel("Number of Tweets")
        plt.ylabel("Sentiment")
        plt.show()

submit = Button(root, text ="Submit", background='#5D8AA8', fg="black", command = mainFunction)

widget.pack()
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
label8.pack()
E8.pack()
label9.pack()
E9.pack()
frame.pack()
submit.pack(side =BOTTOM)
root.mainloop()
