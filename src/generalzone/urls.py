from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^enquiry', views.enquiry, name='enquiry'),
    url(r'^trackorder', views.track_shipment, name='track_shipment'),
    url(r'^complain', views.complain, name='complain'),
    url(r'^login', views.login, name='login'),
    url(r'^career', views.career, name='career'),
    url(r'^saveenquiry', views.saveenquiry, name='saveenquiry'),
    url(r'^savecomplain', views.savecomplain, name='savecomplain'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^search', views.search, name='search')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)