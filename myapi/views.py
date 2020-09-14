from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import *

# Create your views here.
class PeopleAPI(viewsets.ModelViewSet):
	serializer_class = PeopleSerializer
	queryset = People.objects.all()

	def update(self, request, pk):
		people_object = People.objects.get(pk=pk)
		serializer = PeopleSerializer(people_object, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		people_object = People.objects.get(pk=pk)
		people_object.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
