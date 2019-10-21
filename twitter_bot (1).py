import tweepy
import csv
import json

consumer_key = "WeJg0Nz6J71SSa6VhkaagRiil"
consumer_secret = "0Ptd2XgRnU1qWVxDL29PgKUAW7CXlPBQgVtKOvWIdvTWW3a4gd"
access_token = "1070431112223252481-Ln002ZDQZTXrrcY8xXshjX93fA32Xa"
access_token_secret = "ZDMjLGgQt8kUojrgzYO94Xh2EE4Y3GNhHkRRlNV95a2iV"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print( "getting tweets before %s" % (oldest))
		
		#all subsequent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		print('new_tweets', new_tweets[0].text.encode("utf-8"))
<<<<<<< HEAD

		new_string = ""
		for c in new_tweet
			substring = c
			if substring.isalpha():
				new_string = new_string + substring
			else:
				continue

=======
		new_string = ""
		for c in new_tweets:
			substring = ""
			substring = substring + c
			if substring.isalpha():
				new_string = new_string + c
			else:
				continue


>>>>>>> cf52361d68ba355f76a2b262d79a0ae807853ecf
		#HERE iterate through the string and cut it if it is not a character
		#Make sure that you are generating the right file (he should have fixed the endl for you)
		#Including the files in setup. 
		#save most recent tweets
		alltweets.extend(new_string)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print( "...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['id'.encode(),'created_at'.encode(),'text'.encode()])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("BarackObama")
