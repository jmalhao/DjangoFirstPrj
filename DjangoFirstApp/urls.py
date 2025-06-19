from django.urls import path

from . import views

#from django.urls import re_path
#from . import views

urlpatterns = [
    path('', views.main, name='main'),
    #path('', views.DjangoFirstApp, name='DjangoFirstApp'),
    #path('', views.index2, name="index2"),
    path("add/<str:member_name>/", views.add_member, name="add_member"),
    path('index', views.index, name='index'),

    #re_path(r'^$', views.index2, name='index2'),
]