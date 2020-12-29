from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone
TYPE = ( 
    ("Diary", "diary"), 
    ("Journal", "journal"), 

) 
class Journal(models.Model):
	published_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=250,default="default")
	emotion = models.CharField(max_length=50)
	category =models.CharField(max_length=25,choices=TYPE,default="Diary")
	title = models.CharField(max_length=100)
	image = models.TextField()
	def __str__(self):
		return str(self.published_date)+str(self.user.username)

class JournalSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username')
	class Meta:
		model=Journal
		fields=['id','title','published_date','description','username','emotion','image','category']

