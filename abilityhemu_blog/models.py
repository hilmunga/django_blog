# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone

# models for the object post(properties).

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null = True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank= True, null = True)

    #self means they belong to the class Post.
    #methods for publishing date

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title






