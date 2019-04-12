from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
	ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('regular', 'Regular')
    )
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices = ROLE_CHOICES, default="regular")

class Record(models.Model):
	user_id = models.ForeignKey(User, null = False, on_delete=models.CASCADE)
	distance = models.IntegerField(default='0')
	time = models.IntegerField(default='0')
	date = models.DateField(null = False)
