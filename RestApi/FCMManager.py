import firebase_admin
from fcm_django.models import FCMDevice
from firebase_admin import credentials,messaging
from firebase_admin.messaging import Message, Notification



cred = credentials.Certificate("notificationtask-d17db-firebase-adminsdk-gda3i-700c246541.json")
firebase_admin.initialize_app(cred)

def sendNotification(title,msg,devices):
    message=Message(
        notification=Notification(title=title, body=msg)
    )
    return devices.send_message(message)

