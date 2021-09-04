from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from fcm_django.models import FCMDevice
from RestApi.models import BrowserToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def save(self, **kwargs):
        user =User(
            username = self.validated_data.get('username'),
            password=make_password(self.validated_data.get('password'))
        )
        user.save()
class BrowserSerializers(serializers.ModelSerializer):
    class Meta:
        model=BrowserToken
        fields="__all__"
class Tokens(serializers.Serializer):
    token = serializers.CharField(read_only=True,max_length=100)

class FCMDeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model=FCMDevice
        fields="__all__"

class sendMessageSerializers(serializers.Serializer):
    title=serializers.CharField(max_length=50)
    body = serializers.CharField(max_length=100)
    toAll=serializers.BooleanField(required=True)
    tokens=Tokens(many=True,required=False)
