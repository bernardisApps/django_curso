from django.urls import path
from .views import *

app_name = 'favoritos'

urlpatterns = [
    path('crear/', crear),
    path('lista/', lista),
]