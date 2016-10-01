from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
# Create your models here.

class MyUser(models.Model):
	user=models.ForeignKey(User, null=True, unique=True)
	name = models.CharField(max_length=128,unique=True)
	score=models.IntegerField(max_length=100, null=True)
	isRegistered=models.BooleanField(null=False)

	def __unicode__(self):
		return self.pok_name