from django.test import TestCase
from .models import post


class BasicSet(TestCase):

    def test_fields(self):
        Post = post()
        Post.ImgName = "Image Name"
        Post.ImgURL = "https://hddesktopwallpapers.in/wp-content/uploads/2015/08/sunset-images-mountain.jpg"
        Post.ImgDetails = "Image Detail"
        Post.save()

        record = post.objects.get(pk=Post.id)
        self.assertEqual(record, Post)

    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
