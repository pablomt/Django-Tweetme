from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView
	)

urlpatterns = [
	# url(r'^$', RedirectView.as_view(url="/"), ), # /
    url(r'^$', TweetListAPIView.as_view(), name='list-api'), # api/tweet/
    # url(r'^crear/$', TweetCreateView.as_view(), name='create'), # /tweet/create
    # # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1
    # url(r'^(?P<pk>\d+)/actualizar/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    # url(r'^(?P<pk>\d+)/borrar/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]
