from django.contrib import admin
from .models import Enquiry,Complain,Career,LoginInfo

admin.site.register(Enquiry)
admin.site.register(Complain)
admin.site.register(Career)
admin.site.register(LoginInfo)