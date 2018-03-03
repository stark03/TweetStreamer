import tweepy
import time
from .models import Tweet,User

class StreamListener(tweepy.StreamListener):
	
	"""Self-defined Class inheriting the StreamListener class"""	
	def __init__(self, time_limit, keyword):
		self.start = time.time()
		self.limit = time_limit
		self.keyword = keyword
		super(StreamListener, self).__init__()

	def on_status(self, status):
		
		"""Creates Tweet, User models based on the tweets being streamed using the given keyword"""
		if (time.time() - self.start) < self.limit:
			"""checks whether the time of streaming the tweets is under limit or not, 
			   if yes continues to stream, else stops"""


			if hasattr(status, 'retweeted_status') and status.retweeted_status:
				"""Removes the retweets, hence removing duplicates"""
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
				"""Checks whether the User of the streamed tweet is in User table or not, 
				   if yes, ignores, else creates a new entry in the table"""
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
		"""Disconnects if rate limited """
		if(status_code == 420):
			return False
