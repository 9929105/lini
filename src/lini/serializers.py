'''
Created on Nov 8, 2014

@author: Jacob Wan
'''
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from OrderPlacer.models import * 
from django.db.models.fields.related import ManyToManyField


class ExternalIdentifierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExternalIdentifier
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        
class PersonSerializer(serializers.ModelSerializer):
    identifiers =ExternalIdentifierSerializer(many=True,required=False, blank=True, allow_add_remove=True, source="identifiers.all") 
    class Meta:
        model = Person
        dept = 2

class ContentObjectRelatedField():
    def to_representation(self, value):
        if isinstance(value, Person):
            serializer = PersonSerializer(value)
        return serializer.data

class PersonRoles(serializers.ModelSerializer):
    class Meta:
        model = PersonRoles  


class PriceHistorySerializer(serializers.ModelSerializer):   
    class Meta:
        model = PriceHistory
    

class MedicalServiceSerializer(serializers.ModelSerializer):
    pricehistories = PriceHistorySerializer(many=True,required=False, blank=True, allow_add_remove=True)
    class Meta:
        model = MedicalService
        dept = 2
        
class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
           
class EncounterSerializer(serializers.ModelSerializer):
    patient = PersonSerializer(required=True,blank=False, read_only=False)
    provider = PersonSerializer()
    class Meta:
        model = Encounter
        dept =2

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
         

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')



    