'''
Created on Nov 8, 2014

@author: Jacob Wan
'''
from rest_framework import serializers
from django.contrib.auth.models import User
from OrderPlacer.models import * 
        
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        
class PersonSerializer(serializers.HyperlinkedModelSerializer):   
    class Meta:
        model = Person

class PersonRoles(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonRoles  

class MedicalServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalService
        
class SynonymSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Synonym
    
class PriceHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PriceHistory
        depth = 1
        
class EncounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encounter

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
         
class ExternalIdentifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalIdentifier
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


    