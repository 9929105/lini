from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import date
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now_add=True)
    beg_effective_dt = models.DateTimeField(auto_now_add=True)
    end_effecitve_dt = models.DateTimeField(default=date(2199,12,31))
    created_by =  models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by")
    modified_by = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_modified_by")
        
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        super(BaseModel, self).save(*args, **kwargs)
        

class Role(BaseModel):
    role_name = models.CharField(max_length=200)  


class Person(BaseModel):
    person_identifier = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    name_first = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    birthdate = models.DateTimeField(null=True)

class PersonRoles(BaseModel):
    person = models.ForeignKey(Person, related_name="personroles_person")
    role = models.ForeignKey(Role,related_name="peresonroles_role")  

class MedicalService(BaseModel):
    
    display = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    
class Synonym(BaseModel):
    
    service = models.ForeignKey(MedicalService, related_name="synonym_service")
    synonym = models.CharField(max_length=1000)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=1000)

class PriceHistory (BaseModel):
    
    service = models.ForeignKey(MedicalService,related_name="price_service")
    price = models.FloatField(default=0.00)
     
class Encounter(BaseModel):   
    patient = models.ForeignKey(Person,related_name="encounter_patient")
    encntr_dt = models.DateTimeField(auto_now_add=True)
    provider = models.ForeignKey(Person,related_name="encounter_physician")
    followup_dt = models.DateTimeField(null=True)

class Order(BaseModel):
    
    order_identifier = models.CharField(max_length=200)
    patient = models.ForeignKey(Person, related_name="orders_patient")
    service =models.ForeignKey(MedicalService, related_name="order_service")
    price = models.FloatField(default=0)
    price_adjusted_dt = models.DateTimeField(null=True)
    price_adjusted_by = models.ForeignKey(User,null=True)   
    order_dt = models.DateTimeField(auto_now_add=True)
    collect_dt = models.DateTimeField(null=True)
    
    ordered_by = models.ForeignKey(Person, related_name="orders_ordered_by")
    collected_by = models.ForeignKey(Person, related_name="order_collected_by")
    
class ExternalIdentifier(BaseModel):
    ext_identifier = models.CharField(max_length=500)
    issued_by = models.CharField(max_length=200)
    unique_pool = models.CharField(max_length=200)
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
        
 
     

    