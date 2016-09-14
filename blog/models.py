from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    texto = models.TextField()

    @property
    def proximo(self):
        return Post.objects.filter(pk__gt=self.pk).order_by('pk').first()

    @property
    def anterior(self):
        return Post.objects.filter(pk__lt=self.pk).order_by('-pk').first()
