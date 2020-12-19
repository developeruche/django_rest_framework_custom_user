from django.db import models
from user.models import CustomUser


# Create your models here.
""" 
Explantion of the Jwt model:
Jwt will store the jwt-token which is sent to the user in form of rest_framework response
user: The user is a one to noe field so whenever Jwt is sent to the db manager for storeage 
    there wont be a case of a user have more that one Jwt dat stored in the DB that can lead to a security 
    threat
access: This is a token the Server would require of the application before a any request is processed
refresh: This is the token with which the server request for to keep the user login (This convemtionally have longer life span)

"""


class Jwt(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
