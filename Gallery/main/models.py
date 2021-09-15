from django.db import models
from django.db.models import Model
from django.urls import reverse

class post(models.Model):
    ImgName = models.CharField(max_length=100)
    ImgURL = models.URLField(max_length = 200)
    ImgDetails = models.TextField()

    def __str__(self):
        return self.ImgName

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})