from django.shortcuts import render, redirect
from rest_framework.filters import SearchFilter, OrderingFilter
from django.urls import reverse
from django.http import HttpResponse
from .serializers import TweetSerializer, UserSerializer
from .models import Tweet, User
from .streamTweets import StreamListener
from .private import *
import tweepy
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.utils import timezone
import time
from .pagination import TweetLimitOffsetPagination, UserLimitOffsetPagination


auth = tweepy.OAuthHandler(TWITTER_APP_KEY,TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY,TWITTER_SECRET)
api = tweepy.API(auth)

class TweetsView(generics.ListAPIView):

	#queryset = Tweet.objects.all().order_by('-created_at')
	serializer_class = TweetSerializer
	pagination_class = TweetLimitOffsetPagination
	queryset = Tweet.objects.all().order_by('created_at')
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['text','keyword','user']


class UsersView(generics.ListAPIView):
	
	serializer_class = UserSerializer
	pagination_class = UserLimitOffsetPagination
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['screen_name', 'location']
	queryset = User.objects.all()





def StreamTweetsWithKeyword(request, keyword):
	
	s = StreamListener(10, keyword)
	stream = tweepy.Stream(auth = api.auth, listener = s)
	stream.filter(track = [keyword])	
	#time.sleep(4)
	#stream.stop()
	return redirect(reverse('tweet'))




