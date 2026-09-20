from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True) #u can't use same email for different acct
    phone = models.CharField(max_length=20, blank=True) #Phone can be blank. u can enter without phone
    is_email_verified = models.BooleanField(default=False)
