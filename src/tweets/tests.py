from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

# Create your tests here.

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
# Esta funcio se ejecuta primero setUp
    def setUp(self):
        some_random_user = User.objects.create(username="usuarioTest")

    # Esta es la funcon que se va ejecutar al hacer el test
    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = "Some content"
        )
        self.assertTrue(obj.content == "Some content")
        self.assertTrue(obj.id == 1)
        # self.assertEqual(obj.id, 1) # es lo mismo que la linea de arriba
        absolute_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = "Some content"
        )
        absolute_url = reverse("tweet:detail", kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
