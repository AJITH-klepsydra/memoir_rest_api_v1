from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
class Notes(models.Model):
		published_date = models.DateTimeField(auto_now_add=True)
		user = models.ForeignKey(User, on_delete=models.CASCADE)
		description = models.TextField()
		end_date = models.DateTimeField()
		title = models.CharField(max_length=100)
		def __str__(self):
			return str(self.published_date)
		def is_ended(self):
			return self.published_date - self.end_date

class NotesSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username')
	class Meta:
		model=Notes
		fields=['id','title','published_date','description','username','end_date']



