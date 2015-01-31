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

def index(request):
    htlm = "<H1> Order Placer Page.  You Place order here.</H1><HR>"
    return HttpResponse(htlm)

def review(request):
    http= "<HTML><BODY><H1>Please Review the Test Order before Submission</H><HR></BODY></HTML>"
    return HttpResponse(http)

def get_order(request, oid ='0'):
    #http="<HTML><BODY><H1> The Order you have requested ="+oid+"</H1><HR></BODY></HTML>"
    http="<HTML><BODY><H1> The Order you have requested ="+oid+"</H1><HR></BODY></HTML>"
    return HttpResponse(http)

def get_services(request, test_name='ALL'):
    
    response = HttpResponse()
    response.write("<html><body>\n")
    response.write("<h1>Test List<h1><hr>\n")
    
    if test_name == "ALL":
        testList = MedicalService.objects.all()
        for onetest in testList:
            response.write("<li>%s</li>\n" % (onetest.display))
    
    response.write("</body></html>")
    
    return response
                


# Serializers define the API representation.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

class MedicalServiceViewSet(viewsets.ModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class =MedicalServiceSerializer
    
    def post_save(self, obj, created=False):
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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 
    
