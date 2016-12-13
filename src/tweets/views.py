from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.
class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs) # imprime los argumentos que se reciben desde el url
    #     pk = self.kwargs.get("pk") # Se asigna a la variable pk lo que venga del url
    #     print(pk)
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)

        return context



def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(id=pk)
    obj = get_object_or_404(Tweet, pk= pk)
    context = {
        "object": obj
    }

    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request, id=1):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
