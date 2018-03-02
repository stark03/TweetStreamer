from .models import User, Tweet
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):

	class Meta():
		model = Tweet
		fields = ('keyword','created_at', 'id', 'user', 'text', 'retweet_count', 'favorite_count')


class UserSerializer(serializers.ModelSerializer):
	
	class Meta():
		model = User
		fields = ('screen_name', 'followers_count', 'location')






