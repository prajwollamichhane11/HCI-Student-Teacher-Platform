#we need path
from django.urls import path

#we also need the views
from . import views

#we need to map the URLs
#we specified the path
#home is a fucntion on views.py of this app
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add')
]
