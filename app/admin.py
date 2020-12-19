from django.contrib import admin
from .models import TestBlog

admin.site.register((TestBlog, ))
