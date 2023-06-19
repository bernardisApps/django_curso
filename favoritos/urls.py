from django.urls import path
from .views import *

app_name = 'favoritos'  

urlpatterns = [
    path('crear/', crear, name='crear'),
    path('', lista, name='lista'),
    path('borrar/<int:pk>', borrar , name='borrar'),
]