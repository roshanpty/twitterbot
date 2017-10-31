#!/usr/bin/env python
import sys, getopt
import json
import csv
import urllib2
import tweepy
import threading
from time import sleep
import multiprocessing

def trend():
	sleep(5)
	for line in file_lines:
		if line != '\n':
			try:
				api.update_status(hashtag + line)
				print "\n",user + " tweeted with trend hash tag: " + hashtag + line
			except:
				pass
		else:
			pass
		sleep(180)

def rand():
	sleep(10)
	for i in (0,50):
		response = urllib2.urlopen('https://talaikis.com/api/quotes/random/')
		quot = json.load(response)
		tw2 = quot["quote"]+"-"+quot["author"]
		if len(tw2) > 139:
			tw3 = tw2[0:140]
 			api.update_status(tw3)
			print "\n",user,"tweeted random quote: ", tw3
		else:
			api.update_status(tw2)
			print "\n",user,"tweeted random quote: ", tw2
		sleep(120)

def retw():
	sleep(15)
	for tweet in tweepy.Cursor(api.search, q= hashtag).items(50):
		try:
			print "\n", user, "retweeted a tweet by: @", tweet.user.screen_name
			tweet.retweet()
			tweet.favorite()
		except tweepy.TweepError as e:
			print(e.reason)
		sleep(240)


def randretw():
	sleep(20)
	for tweet in tweepy.Cursor(api.search, q= 'science').items(50):
		try:
			print "\n", user, "retweeted a tweet by: @", tweet.user.screen_name
			tweet.retweet()
			tweet.favorite()
		except tweepy.TweepError as e:
			print(e.reason)
		sleep(300)

def botaction():
		# Function which controls the actions of each individual bot
	global user
	global consumer_key
	global consumer_secret
	global access_token
	global access_token_secret
	global auth
	global api

	user = account['username']
	consumer_key = account['consumer_key']
	consumer_secret = account['consumer_secret']
	access_token = account['access_token']
	access_token_secret = account['access_token_secret']
	print user

	# Authenticate accounts on twitter api using tweepy
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	print "authenticated",user

	for fun in (trend,rand,retw,randretw):
		print "Creating processes for %s" % fun
#		t = threading.Thread(target=fun)
#    	threads.append(t)
#    	t.start()
		k = multiprocessing.Process(target=fun)
		jobs.append(k)
		k.start()
	
def usage():
	print "Usage: python bot.py -c credentials.csv -f tweets.txt -h hashtagtotrend"


# Reading arguments for credentials file, trendtweets file and hashtag
	
credentials = ''
tweetfile = ''
hashtag = ''

try:
	myopts, args =  getopt.getopt(sys.argv[1:], "c:f:h:")
	
except getopt.GetoptError as err:

	print str(err)
	usage()
        sys.exit(2)

for o, a in myopts:
	if o == "-c":
		credentials = a
	elif o == "-f":
		tweetfile = a
	elif o == "-h":
		hashtag = "#"+a+" "
	else:
		usage()

# Open a file with a set of tweets and read them line by line

my_file = open(tweetfile, 'r')
file_lines = my_file.readlines()
my_file.close()

# Fetching user credentials for users from credentials CSV file

credstore = csv.DictReader(open(credentials, 'rb'))
dict_list = []

for y in credstore:
	dict_list.append(y)		# Loading the CSV into a python dictionary

jobs = []
print "Credentials loaded"
for account in dict_list:
	p = multiprocessing.Process(target=botaction)
	jobs.append(p)
	p.start()
