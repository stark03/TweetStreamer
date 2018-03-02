from django.db import models

class User(models.Model):
	Id = models.BigIntegerField()
	name = models.CharField(max_length = 100)
	screen_name = models.CharField(max_length = 100, null = True, blank = True)
	url = models.CharField(max_length = 200, null = True, blank = True)
	description = models.TextField(null = True)
	followers_count = models.IntegerField(null = True)
	statuses_count = models.IntegerField(null = True)	

class Tweet(models.Model):
	created_at = models.TextField()
	id = models.BigIntegerField(primary_key = True)
	id_str = models.CharField(max_length = 200)
	text = models.TextField()
	user = models.BigIntegerField(null = True)
	retweet_count = models.IntegerField(null = True)
	favorite_count = models.IntegerField(null = True)



	
	
		













