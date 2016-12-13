from django.contrib import admin

from .forms import TweetModelForm
from .models import Tweet
# Register your models here.

class TweetModelAdmin(admin.ModelAdmin):
	form = TweetModelForm


admin.site.register(Tweet, TweetModelAdmin)