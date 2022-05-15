import json
from urllib import response
from MySQLdb import IntegrityError
from click import password_option
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pyrebase
import requests
 
 
config={ 
    'apiKey': "AIzaSyBgsSN3muLZz99OEn3igm0tUbm57RJrmlI",
  'authDomain': "cs-551-project.firebaseapp.com",
  'databaseURL':'https://cs-551-project-default-rtdb.firebaseio.com/',
  'projectId': "cs-551-project",
  'storageBucket': "cs-551-project.appspot.com",
  'messagingSenderId': "691181576168",
  'appId': "1:691181576168:web:9c2639efac439841a64e5d",
  'measurementId': "G-70KGTXWVJJ"
  }
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()

@csrf_exempt 
def signIn(request):
    if request.method=='POST':
        auth_data = json.loads(request.body.decode("utf-8"))
        email = auth_data.get('email')
        password = auth_data.get('password')
        result={}
        try:
        # if there is no error then signin the user with given email and password
            user=authe.sign_in_with_email_and_password(email,password)
            result.update(user)
            session_id=user['idToken']
            request.session['userId']=str(session_id)
            request.session.modified = True
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            result.update({"Error":error}) 
            
        
        return JsonResponse(result,safe=False)

@csrf_exempt
def signUp(request):
     auth_data = json.loads(request.body.decode("utf-8"))
     email = auth_data.get('email')
     password = auth_data.get('password')
     name = request.POST.get('name')
     result={}
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,password)
        uid = user['localId']
        request.session['uid']=uid
        result.update({"Email":email,"Password":password})
     except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            result.update({"Error":error})
     return JsonResponse(result,safe=False)

@csrf_exempt
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return JsonResponse('Logout',safe=False)
 