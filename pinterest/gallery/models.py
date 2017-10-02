# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
	"""docstring for ClassName"""
	img = models.ImageField(upload_to = 'upload')
	description = models.TextField()
	created = models.DateTimeField(auto_now_add = True)

class User(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	isSeller = models.BooleanField(default=False)
	user_id = models.AutoField(primary_key=True)
	password = models.CharField(max_length = 100)
	created_date = models.DateTimeField(auto_now_add = True)
		