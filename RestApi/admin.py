from django.contrib import admin

# Register your models here.
from RestApi.models import BrowserToken
from fcm_django.models import FCMDevice
admin.site.register(BrowserToken)
