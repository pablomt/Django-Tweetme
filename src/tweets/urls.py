from django.conf.urls import url
from .views import (
	tweet_detail_view,
	tweet_list_view,

	TweetDetailView,
	TweetListView,
	TweetCreateView,
	TweetUpdateView,
	TweetDeleteView
	)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    url(r'^crear/$', TweetCreateView.as_view(), name='create'), # /tweet/create
    # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1
    url(r'^(?P<pk>\d+)/actualizar/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    url(r'^(?P<pk>\d+)/borrar/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]
