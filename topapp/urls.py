from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('materiais', materiais, name='materiais'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('criarusuario', createUser, name='criarusuario'),
]

