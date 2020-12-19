from django.urls import path
from .views import LoginView, RegisterView, RefreshView, PreRestPassword, ResetPassword

urlpatterns = [
    path("login", LoginView.as_view()),
    path("register", RegisterView.as_view()),
    path("refresh", RefreshView.as_view()),
    path("pre", PreRestPassword.as_view()),
    path("reset/<reset_url>", ResetPassword.as_view()),
]
