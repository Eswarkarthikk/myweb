from . import views
from django.urls import path

urlpatterns=[
    path('',views.mainpage,name='mainpage'), 
    path('upload_image',views.upload_image,name='upload_image')
]

