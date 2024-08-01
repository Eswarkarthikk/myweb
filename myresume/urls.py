from . import views
from django.urls import path

urlpatterns=[
    path('',views.mainpage,name='mainpage'), 
    path('projects1/',views.projects1,name='projects1'),
    path('projects2/',views.projects2,name='projects2'),
    path('projects3/',views.projects3,name='projects3'),
    path('experence1/',views.experience1,name='experience1'),
    path('experence2/',views.experience2,name='experience2'),
    path('experence3/',views.experience3,name='experience3'),
    path('aboutme/',views.aboutme,name='aboutme'),
    path('certifications/',views.certifications,name='certifications')
    
]

