from . import views
from django.urls import path
urlpatterns = [

    path('bags',views.bags,name='bags'),
    path('dress', views.dress, name='dress'),
    path('shoes', views.shoes, name='shoes')

    ]

