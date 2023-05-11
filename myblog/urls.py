from django.urls import path
from myblog.views import  List, detailView
from . import views

urlpatterns = [
    path('index/', views.index, name='index.html'),
    path('about/', views.about, name='about.html'),
    #path('contact/', views.Contact, name='contact.html'),
    path('search/', views.search, name='search'),
    #path('user/', views.user, name='user'),
    path('detail/<slug:slug>', detailView, name='detailView'),
    path('', List.as_view(), name='acceuil'),
    path('', List.as_view(), name='ABS blog')
]