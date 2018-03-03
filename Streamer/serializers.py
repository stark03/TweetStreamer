from .models import User, Tweet
from rest_framework import serializers

class TweetSerializer(serializers.ModelSerializer):
	""" Serializer for model Tweet"""
	class Meta():
		model = Tweet
		#fields = ('keyword','created_at', 'id', 'user', 'text', 'retweet_count', 'favorite_count')
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	
	"""Serializer for model User"""
	class Meta():
		model = User
		fields = '__all__'






