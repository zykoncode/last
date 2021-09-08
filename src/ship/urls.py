from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('generalzone.urls')),
    url(r'^adminzone/', include(('adminzone.urls', 'adminzone'), namespace='adminzone')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
