from django.db import models

# Create your models here.
from pyasn1.compat.octets import null
from rest_framework.authtoken.admin import User


class BrowserToken(models.Model):
    token = models.CharField(null=False, blank=False, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} in {self.date} '

class Notification(models.Model):
    message=models.CharField(null=True,blank=True,max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isSeen=models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)