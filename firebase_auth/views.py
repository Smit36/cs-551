from django.shortcuts import render
import pyrebase
 
 
config={    
  "type": "service_account",
  "project_id": "cs-551-project",
  "private_key_id": "6cb11295efdd07c76f8e4e5f5d0a4e61e94b76b3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDcfSZVOhsxIwMx\nH8ZojSh6TnUZjRX4vR3tVEMIv0dOLRHntNOYK00Tvxa3FfUfOuh5fnm02SDTxpVl\n3VaiMEDRPkqzzOJ06pZOVzo5sHyMnhx5m3OZy6YJke69Hum/MIAGllHA1nMyyV1E\nlOohfjiRNcy7NsEr7cUYTam/Rf1mcaDx8mvEeA8VqBEN+jU9gY9n7oPZJy9Rm6zL\nVblO7fovUrB3hqNv39ncmAxbHf3/WCQbpyV6a7ldUUVGVaxJPiwv0CUw6fZmVj1S\nGSVedoKmAuhO+CF1qeO0Zq4ZCfH9BNcprOV43Rf3M7FGPVLWg6zUlodMrVLCD7Ai\nbn2VPWHRAgMBAAECggEAAc2oKo0/fLkFdkly1WTBvMzHXl8TxN+0rJ3pL/JS/Bn4\nOy5d2Qf2ojCoilBYEmpDxGNVclGpzvIu5+EKgpYMMoZ965mVuxMbUqSHrKa5U30H\nyEUOPFSx8pUN/ftisNwSYyJDJLxbJBlAIQ2zY73GRlh7v2tQ2h1uNulVRb9hWiPv\nbNhXAA7tc/m300pF2vF+7QmDdL+S0EJHkAutLHRWVEidRvL+ypiUVqVFjvH40kAL\n5hssjBhqstyLrg+lW5p5YGxw1R+7/XoLaT5HIpWFgTnj3ha/bmkDNt94MddPvNKe\nXaC1xgEgiFZaSooPxq/CJh7mW81NQEbZJe1W1+0GWQKBgQD08VSPLKHEWkPlKhiR\nints/DMpH+pt5Y88//Il/Lw+wBvhqRmHJj+JhLSHl5YRb3MX10f12MTq5ezxGSme\nGzIuf4JZZeIJTv08E1/a2lG9JZklw9q2LzR2CtOABNvS0hqrYmIAo7O8fBI0Ye7m\nO+iwKid8mMOQriSwxIrWzJGDuQKBgQDmcThEbwDEV/PaN6KyqnkIfKoNpVfhebfM\nvq2b6A1IRqvDpXP/W6PxtLhToT2MNA4EEQeRV3zkurOZNwDax2a8NotecaD+CfMr\nHnJtGNKtJTVXeDhrT4aWgkgWn0KPpUg39XsXzIS9WHDEYvt0DNhiroVuM8XG0Pbl\ng2dUi3uK2QKBgQCTft8UeCPRQSmxTXAN8/3u2s9T7EwWcS2X5efCyDXy82vWryUY\nJQgNn0O2gqlzRlFgAdrrR+UMLfhIFobhFi9ZoJ61hoxeXppPGruV5fFinMlj3FRP\ncI1+p3ZEmKhmgu5cVZn+GJWa4ntz36UkLt8ndbrhZHwfGz4s061nOzhEwQKBgDP5\nIySkGHswDwqPc71yH1wfqcbsHLb42dBuzP8VxjEf50t3/IKCa6ZvCQernRMLBoI6\nSQepwLxhs3IB6sptIKmgb6x8WkARhGucMViTuahddPtmXOsvA37coV+gycVWFMSy\nM/H5KZL+6GgSnv3ci80t6WAigx/FL3oyOdLippl5AoGACXO4gtyZxIspSpAxHvUD\n3+MYNqikM8M4lm3lTL/UA93B7J9zVTbg7kLSjmyx2MihMIA/d1sezuSj2P0QwKOT\np8D/Y4y0VOn/ERVQS1EPRzUBbForcszc3UPwLHBR7L61qtgHfhGET3KVFYW3NGzn\nLDK9V1CCoXGnFyTjY+y2MNg=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-6vt7z@cs-551-project.iam.gserviceaccount.com",
  "client_id": "101302994727469170231",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6vt7z%40cs-551-project.iam.gserviceaccount.com"
}
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()

# def signIn(request):
#     return render(request,"Login.html")
# def home(request):
#     return render(request,"Home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})