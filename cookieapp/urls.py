from django.urls import path
from .views import setcookie, getcookie, deletecookie

urlpatterns = [
    path('setcookie/', setcookie, name='setcookie'),
    path('getcookie/', getcookie, name='getcookie'),
    path('deletecookie/', deletecookie, name='deletecookie')
]
