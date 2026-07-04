from django.db import models
from accounts.models import User

class Complaint(models.Model):

    citizen = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=50,default="Pending")

    mp_reply = models.TextField(null=True,blank=True)