from django.urls import path
from .views import TestBlogView, TestBlogUpdateView

urlpatterns = [
    # This is a not login projected route
    path("", TestBlogView.as_view(), name="list_create_route"),
    # This is a login protected route
    path("update/<str:slug>", TestBlogUpdateView.as_view(),
         name="blog_update_route"),
]
