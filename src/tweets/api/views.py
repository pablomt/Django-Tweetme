from rest_framework import generics
from django.db.models import Q
from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    # funcion para poder ejecutar una busqueda
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        print(query)
        return qs
