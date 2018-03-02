from django.db import models

class User(models.Model):
	Id = models.BigIntegerField()
	name = models.CharField(max_length = 100)
	screen_name = models.CharField(max_length = 100)
	url = models.CharField(max_length = 200, null = True, blank = True)
	description = models.TextField(null = True)
	followers_count = models.IntegerField(null = True)
	statuses_count = models.IntegerField(null = True)	

class Tweet(models.Model):
	keyword = models.CharField(max_length = 30, null = True)
	created_at = models.CharField(max_length = 100, null = True)
	id = models.BigIntegerField(primary_key = True)
	text = models.TextField()
	user = models.BigIntegerField(null = True)
	retweet_count = models.IntegerField(null = True)
	favorite_count = models.IntegerField(null = True)



	
	
		













