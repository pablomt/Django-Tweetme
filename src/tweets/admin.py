from django.contrib import admin

from .forms import TweetModelForm
from .models import Tweet
# Register your models here.

class TweetModelAdmin(admin.ModelAdmin):
	# form = TweetModelForm # se comenta deido a que no se a modificar nada
	list_display = ['id', 'content',]
	class Meta:
		model = Tweet

admin.site.register(Tweet, TweetModelAdmin)
