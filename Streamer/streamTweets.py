import tweepy
import time
from .models import Tweet,User

class StreamListener(tweepy.StreamListener):
	
	def __init__(self, time_limit):
		self.start = time.time()
		self.limit = time_limit
		super(StreamListener, self).__init__()

	def on_status(self, status):

		if (time.time() - self.start) < self.limit:
			k = Tweet.objects.create(
				id = status.id,
				id_str = status.id_str,
				created_at = status.created_at,
				user = status.user.id,
				text = status.text,
				retweet_count = status.retweet_count,
				favorite_count = status.favorite_count,
				
			)
			return True
		else:
			return False

	def on_error(self,status_code):
		if(status_code == 420):
			return False
