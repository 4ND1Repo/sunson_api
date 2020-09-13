from django.db import models

# Create your models here.

class People(models.Model):
	nama = models.CharField(max_length=100)
	alamat = models.CharField(max_length=1000)
	status = models.BooleanField(default=0)
