from django.urls import path
from . import views


# URL configuration
urlpatterns = [
    # we don't need
    path('kire/', views.say_hello)
    # path('playground/hello/', views.say_hello)
]