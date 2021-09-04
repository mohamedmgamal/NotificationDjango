from django.contrib.admin.views.decorators import staff_member_required
from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from RestApi import FCMManager
from RestApi.serializers import UserSerializer, BrowserSerializers, sendMessageSerializers,FCMDeviceSerializers


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.all().filter(key=request.data.get('token'))
    print("request.data.get('token')")
    try:
        token.delete()
        return Response(data={
            "message": "logout successfully"
        }, status=status.HTTP_200_OK)
    except Exception:
        return Response(data={
            "Error":Exception
        },status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def signUp(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                "success": True,
                "message": "New user added successfully "
            }, status=status.HTTP_201_CREATED)
        return Response(data={
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def sendToken(request):
    FCMDevice.objects.filter(user=request.data["user"]).delete()
    serializer = FCMDeviceSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "token added successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@staff_member_required
def sendMessage(request):
    serializer = sendMessageSerializers(data=request.data)
    if(serializer.is_valid()):
        validatedData = serializer.validated_data
        if validatedData.get("toAll"):
          data  = FCMDevice.objects.all()
        else:
            data = (FCMDevice.objects.filter(registration_id=validatedData.get("token")))
            if not data:
                return Response(data={
                    "success": False,
                    "errors": "Error in sending Messages "
                }, status=status.HTTP_400_BAD_REQUEST)
        try:
            response = FCMManager.sendNotification(validatedData.get("title"), validatedData.get("body"), data)
            print(response)
            return Response(data={
                    "success": True,
                    "message": "Messages sent successfully"
                }, status=status.HTTP_201_CREATED)
        except:
            return Response(data={
                "success": False,
                "errors": "Error in sending Messages "
            }, status=status.HTTP_400_BAD_REQUEST)


