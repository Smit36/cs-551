
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    # path('admin/', admin.site.urls),
    # Here we are assigning the path of our url
    path('signin', views.signIn),
    path('signup', views.signUp),
    path('logout', views.logout)   
]