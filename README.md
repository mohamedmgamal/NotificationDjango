# Notification using Django

## Description

simple notification system using djagno as backend and vanilla js in front

## Getting Started

### Dependencies

https://fcm-django.readthedocs.io/en/latest/

### Installing

* just add needed Dependencies
* python manage.py makemigrations 
* python manage.py migrate


### Descriptions
* any user can login and sjgn Up useing simple login and sign Up endpoint ; done in back and front 
* after login user will send fcm_token for individual messaging ; done only in back 
* only staff can use endpoint sendMessage to send messages to only one devises or to all using "toAll" indicator ; done only in back 
* after front receive message and update request will be send to back to update message statue
