from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import NotesSerializer
from .models import Notes
from rest_framework.permissions import AllowAny 

@api_view(['POST','GET'])
def NotesPOST(request):
	if request.method == "POST":
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		Notes.objects.create(user = request.user,description=request.body['description'],
								title=body['title'],end_date=body['end_date'])
		return Response(data="Object created", status=status.HTTP_200_OK)
	else:
		notes=request.user.notes_set.all().order_by('published_date')
		serializer = NotesSerializer(notes,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def NotesGET(request,pk):
	try:
		note = request.user.notes_set.get(pk = pk)
	except Notes.DoesNotExist:
		return Response("Note does not exist",status=status.HTTP_404_NOT_FOUND)
	if request.method=='DELETE':
		note.delete()
		return Response("Object deleted",status=status.HTTP_202_ACCEPTED)
	elif request.method=="PUT":
		note.description = request.data['description']
		note.title = request.data['title']
		note.end_date = request.data['end_date']
		note.save()
		
	serializer = NotesSerializer(note)
	return Response(serializer.data, status=status.HTTP_200_OK)