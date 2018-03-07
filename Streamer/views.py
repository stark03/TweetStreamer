from django.shortcuts import render, redirect
from rest_framework.filters import SearchFilter,OrderingFilter
from django.urls import reverse
from django.http import HttpResponse
from .serializers import TweetSerializer, UserSerializer
from .models import Tweet, User
from .streamTweets import StreamListener
from .private import *
import tweepy
from rest_framework import generics
from django.utils import timezone
import time
import csv
from .pagination import TweetLimitOffsetPagination, UserLimitOffsetPagination

"""tweepy authentication, takes a pair of keys and tokens from file private.py"""
auth = tweepy.OAuthHandler(TWITTER_APP_KEY,TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY,TWITTER_SECRET)
api = tweepy.API(auth)

class TweetsView(generics.ListAPIView):
	
	"""View for model Tweet inheriting the genric List API View"""
	serializer_class = TweetSerializer
	pagination_class = TweetLimitOffsetPagination
	queryset = Tweet.objects.all()
	filter_backends = [SearchFilter, OrderingFilter] 
	search_fields = ['text','keyword','user']  


class UsersView(generics.ListAPIView):
	
	"""View for model User inheriting the generic List API View"""
	serializer_class = UserSerializer
	pagination_class = UserLimitOffsetPagination
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['screen_name', 'location']
	queryset = User.objects.all()


def StreamTweetsWithKeyword(request, keyword, time_limit):
	
	"""Triggers the Streaming API for streaming tweets,
	
		parameters : keyword - the keyword for which the tweets are to be streamed,
			     time_limit - the amount of time for the tweets to stream
	"""
	s = StreamListener(time_limit, keyword)
	stream = tweepy.Stream(auth = api.auth, listener = s)
	stream.filter(track = [keyword])	
	return redirect(reverse('tweets'))


def exportAsCSV(request):

	""" Generates a csv file of all the tweet objects with some handpicked important fields"""
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="tweets.csv"'
	
	"""Some importanat handpicked fields, can add any no. of fields"""

	imp_fields = ['created_at', 'text', 'retweet_count', 'favorite_count']
	writer = csv.writer(response)
	writer.writerow(imp_fields)
	q = Tweet.objects.all()		#Can add anyqueryset in place of q
	for x in q:
		writer.writerow([
			x.created_at,
			x.text,
			x.retweet_count,
			x.favorite_count,	
		])

	return response
