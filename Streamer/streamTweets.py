import tweepy
import time
from .models import Tweet,User

class StreamListener(tweepy.StreamListener):
	
	def __init__(self, time_limit, keyword):
		self.start = time.time()
		self.limit = time_limit
		self.keyword = keyword
		super(StreamListener, self).__init__()

	def on_status(self, status):

		if (time.time() - self.start) < self.limit:
			


			if hasattr(status, 'retweeted_status') and status.retweeted_status:
				return 	
			k = Tweet.objects.create(
				keyword = self.keyword,
				id = status.id,
				created_at = status.created_at,
				user = status.user.id,
				text = status.text,
				retweet_count = status.retweet_count,
				favorite_count = status.favorite_count,
			
			)
			
			try:
				t = User.objects.filter(identity = status.user.id).count()
				if t:	
					print("here")
					pass
				else:
					u = User.objects.create(
						identity = status.user.id,
						name = status.user.name,
						screen_name = status.user.screen_name,
						followers_count = status.user.followers_count,
						statuses_count = status.user.statuses_count,	
						friends_count = status.user.friends_count,
						url = status.user.url,
						description = status.user.description,
						location = status.user.location,
					)
			except User.DoesNotExist :
				pass
			return True
		else:
			return False

	def on_error(self,status_code):
		if(status_code == 420):
			return False
