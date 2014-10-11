import tweepy
import pymongo


access_token="97889597-Zk3Qk9ODlvvqIQXvdZSdlNYtZ4ToWxNbDZlsHW0rI"
access_secret="bYQfeRigzVIgLxkgInkW5L0ZZFBA46uMYxcQOOIg"
consumer_key="QvkiReKCHNKcHn3pGrEzQ"
consumer_secret="EV9vdMRfuT2AQlSNPJW4LhDAyOe0z1mAZYqHJNkPH7g"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print status , "\n"
		data = status._json
		self.db = pymongo.MongoClient().Android
		self.db.SampleTweets.save(data)

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True 

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True 

if __name__ == '__main__':
	sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
	sapi.filter(track=['android','ios'])


