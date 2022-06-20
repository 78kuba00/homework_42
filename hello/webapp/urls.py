from django.urls import path

from webapp.views import  calculate

urlpatterns = [
    path('', calculate),
]