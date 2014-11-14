from django.contrib import admin

from OrderPlacer.models import Person, MedicalService, Order, Encounter


admin.site.register(Person)
admin.site.register(MedicalService)
admin.site.register(Order)
admin.site.register(Encounter)
