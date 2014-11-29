from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from lini.views import * 




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'MedicalService',MedicalServiceViewSet)
router.register(r'Encounter',EncounterViewSet)
router.register(r'Order',OrderViewSet)
router.register(r'PriceHistory',PriceHistoryViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lini.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^orderplacer/$', 'lini.views.index'),
#     url(r'^orderplacer/review/$','lini.views.review'),
#     url(r'^orderplacer/review/(?P<oid>\d+)/$','lini.views.get_order'),
#     url(r'^orderplacer/orderables/(?P<test_name>[A-Za-z]+)/$','lini.views.get_orderables'),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
)