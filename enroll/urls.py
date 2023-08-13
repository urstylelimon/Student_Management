from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('show/',views.show,name = 'show'),
    path('add/',views.add,name = 'add'),
    path('delete/',views.delete,name = 'delete'),
    path('update/',views.update,name = 'update'),
]