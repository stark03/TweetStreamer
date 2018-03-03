from django.conf.urls import url
from django.urls import path
from Streamer import views

urlpatterns = [
	
	url(r'^tweets/$', views.TweetsView.as_view(), name = 'tweets'),
	url(r'^users/$', views.UsersView.as_view(), name = 'users'),
	path('keyword/<str:keyword>/<int:time_limit>/', views.StreamTweetsWithKeyword),
	path('csv/',views.exportAsCSV),

]






