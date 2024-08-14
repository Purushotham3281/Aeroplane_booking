from django.urls import path
from booking import views

urlpatterns=[
    path("Home",views.fun1),
    path("detail",views.fun2)
]