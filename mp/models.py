from django.db import models
from accounts.models import User

class ParliamentSpeech(models.Model):

    mp = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    speech_text = models.TextField()

    date = models.DateField(auto_now_add=True)

    summary = models.TextField(blank=True,null=True)