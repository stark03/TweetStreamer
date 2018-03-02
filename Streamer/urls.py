from django.conf.urls import url
from django.urls import path
from Streamer import views

urlpatterns = [
	
	url(r'^tweet/$', views.ClassBasedView.as_view(), name = 'tweet'),
	path('keyword/<str:keyword>/', views.StreamTweetsWithKeyword),

]






