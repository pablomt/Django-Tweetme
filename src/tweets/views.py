from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.

# Create Class base view
# Si el suario va poder ver el contenido pero no publicar sin antes logearse se utiliza FormUserNeededMixin
# Si el suario no va poder ver el contenido sin antes logearse LoginRequiredMixin
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweet/create'

    # Se comenta debido a que se crea un archivo mixin para verificar que el usuario este logeado
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


# Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = '/tweet/'
    # Si no se define success_url busca get_absolute_url definido en el model si no error
    login_url = '/admin/'


# Delete View
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    # reverse_lazy permite una url mas dinamica, utiliza namespace(nombre de app):nombre de url
    success_url = reverse_lazy("tweet:list")



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
    # queryset = Tweet.objects.all() Se comenta porque ahora tambien se incluira una busqueda

    # funcion para poder ejecutar una busqueda
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        print(query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        # Se agrega el form al cntext
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
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
