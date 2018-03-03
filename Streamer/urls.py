from django.conf.urls import url
from django.urls import path
from Streamer import views

urlpatterns = [
	
	url(r'^tweets/$', views.TweetsView.as_view(), name = 'tweets'), #lists the streamed tweets
	url(r'^users/$', views.UsersView.as_view(), name = 'users'), #lists the users of the streamed tweets
	path('keyword/<str:keyword>/<int:time_limit>/', views.StreamTweetsWithKeyword),  #triggers the Streaming API 
	path('csv/',views.exportAsCSV), #exports the tweets data as CSV

]






