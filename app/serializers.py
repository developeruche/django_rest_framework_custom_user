from rest_framework import serializers
from .models import TestBlog


class TestBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBlog
        fields = "__all__"
