from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestBlogSerializer
from rest_framework import generics
from .models import TestBlog
from gateway.authentication import Authentication
from rest_framework.permissions import IsAuthenticated

# Not protected route


class TestBlogView(generics.ListCreateAPIView):
    queryset = TestBlog.objects.all()
    serializer_class = TestBlogSerializer

# Protected Route


class TestBlogUpdateView(generics.UpdateAPIView):
    """ 
    # By adding this few lanes of code you would be able to make the view a login required route
        authentication_classes = [Authentication]
        permission_classes = [IsAuthenticated]
    """
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = TestBlog.objects.all()
    serializer_class = TestBlogSerializer
    lookup_field = 'slug'
