from .models import User, Tweet
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):

	class Meta():
		model = Tweet
		fields = ('created_at', 'id', 'id_str', 'user', 'text', 'retweet_count', 'favorite_count')








