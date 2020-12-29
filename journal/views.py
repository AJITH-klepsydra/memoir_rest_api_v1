from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import JournalSerializer
from .models import Journal
from rest_framework.permissions import AllowAny 
import json
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
	date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	message = 'clock in server is live current time is '
	return Response(data=message+date, status=status.HTTP_200_OK)

@api_view(['POST','GET'])
def journalPOST(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		Journal.objects.create(user = request.user,description=body['description'],
									category=body['category'],title=body['title'],
									emotion=body['emotion'], image=body['image'])
		return Response(data="Object created", status=status.HTTP_201_CREATED)
	else:
		journals=request.user.journal_set.all().order_by('published_date')
		serializer = JournalSerializer(journals,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def journalGET(request,pk):
	try:
		journal = request.user.journal_set.get(pk = pk)
	except Journal.DoesNotExist:
		return Response("Journal does not exist",status=status.HTTP_404_NOT_FOUND)
	if request.method=='DELETE':
		journal.delete()
		return Response("Object deleted",status=status.HTTP_202_ACCEPTED)
	elif request.method=="PUT":
		journal.description = request.data['description']
		journal.title = request.data['title']
		journal.emotion = request.data['emotion']
		journal.category = request.data['category']
		journal.save()	
	serializer = JournalSerializer(journal)
	return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET'])
def journalCAT(request,val):
	if val in ['d','diaries','diary','2']:
		journals = request.user.journal_set.all().filter(category='d').order_by('published_date')
		serializer = JournalSerializer(journals,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif val in ['j','journals','journal','1']:
		journals = request.user.journal_set.all().filter(category='j').order_by('published_date')
		serializer = JournalSerializer(journals,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)	
	else:
		return Response("Journal does not exist",status=status.HTTP_404_NOT_FOUND)


