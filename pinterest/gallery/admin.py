# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image
from .models import User

admin.site.register(Image)
admin.site.register(User)