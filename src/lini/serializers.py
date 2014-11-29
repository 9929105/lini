'''
Created on Nov 8, 2014

@author: Jacob Wan
'''
from rest_framework import serializers
from django.contrib.auth.models import User
from OrderPlacer.models import * 
from django.db.models.fields.related import ManyToManyField
        
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        
class PersonSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Person

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
          
        
class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
           
class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
         
class ExternalIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalIdentifier
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


    