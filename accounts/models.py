from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('citizen','Citizen'),
        ('mp','MP'),
        ('admin','Admin'),
    )

    role = models.CharField(max_length=10,choices=ROLE_CHOICES)