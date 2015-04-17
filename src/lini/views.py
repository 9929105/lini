from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from lini.serializers import *
from OrderPlacer.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import pdb
from lib2to3.fixer_util import String
from httplib import CREATED
from django.db.models.query import QuerySet
from rest_framework import generics
import django_filters
                
# Serializers define the API representation.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
        
    def post_save(self, obj, created=False):
        pid = ExternalIdentifier()
        pid.content_type = ContentType.objects.get_for_model(Person)
        pid.modified_by = obj.modified_by
        pid.created_by = obj.created_by
        pid.identifier = obj.identifier
        pid.object_id = obj.id
        pid.save()

         
class ExternalIdentifierViewSet(viewsets.ModelViewSet):
    queryset=ExternalIdentifier.objects.all()
    serializer_class=ExternalIdentifierSerializer  

class PersonIdentifierViewSet(viewsets.ModelViewSet):
    queryset=ExternalIdentifier.objects.filter(content_type=ContentType.objects.get_for_model(Person))
    serializer_class=ExternalIdentifierSerializer
        
class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

class MedicalServiceViewSet(viewsets.ModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class =MedicalServiceSerializer

    def post_save(self, obj, created=False):
        print "post_save:"
        print obj.id
        ph = PriceHistory() 
        ph.modified_by = obj.modified_by
        ph.created_by = obj.created_by
        ph.service = obj
        ph.price = obj.price
        ph.save()
     


class SynonymViewSet(viewsets.ModelViewSet):
    queryset = Synonym.objects.all()
    serializer_class = SynonymSerializer

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    filter_fields = ('id','patient', 'provider')
    
    def per_save(self,obj,created=False):
        obj.patient.save()
        print obj.patient.id
        print obj.patient.name_last+","+obj.patient.name_first
        
    def post_save(self, obj, created=False):
        print obj.patient.id
        obj.patient.save()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

        
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 
    
