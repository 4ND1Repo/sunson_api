from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

# Create your views here.
class PeopleAPI(viewsets.ModelViewSet):
	serializer_class = PeopleSerializer
	queryset = People.objects.all()[:5]
