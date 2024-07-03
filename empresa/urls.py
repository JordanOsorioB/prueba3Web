from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('servicios', views.Servicios, name="servicios"),
    path('quienesSomos', views.QuienesSomos, name="quienesSomos")
]

