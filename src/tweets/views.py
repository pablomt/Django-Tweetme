from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin

# Create your views here.

# Create Class base view
# Si el suario va poder ver el contenido pero no publicar sin antes logearse se utiliza FormUserNeededMixin 
# Si el suario no va poder ver el contenido sin antes logearse LoginRequiredMixin
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create'
    login_url = '/admin/'

    # Se comentda debido a que se crea un archivo mixin para verificar que el usuario este logeado
    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     # Se valida si el usuario esta autenticado, esta es la primer forma de validar 
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         # Se muestra error en el tamplate
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["El usuario debe estar logeado para continuar"]) 
    #         return self.form_invalid(form) # form_invalid(form) es un metodo de las vistas basadas en clases

        

# Create Function base view 
def create_view_tweet(request):
    form = TweetModelForm(request.POST or None) # render the form

    #Se verifica si todo esta correcto
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user # se asigna automaticamente el usuario al field user
        instance.save()

    # se assigna el form a context para mostrarlo
    context = {
        "form": form
    }

    return render(request, "tweets/create_view.html", context)


# Detail Class base View
class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs) # imprime los argumentos que se reciben desde el url
    #     pk = self.kwargs.get("pk") # Se asigna a la variable pk lo que venga del url
    #     print(pk)
    #     return Tweet.objects.get(id=pk)


# List Class base View
class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)

        return context


# Detail function base view
def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(id=pk)
    obj = get_object_or_404(Tweet, pk= pk)
    context = {
        "object": obj
    }

    return render(request, "tweets/detail_view.html", context)


# List function base view
def tweet_list_view(request, id=1):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
