from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('materiais', materiais, name='materiais'),
    path('materiais/cadastro/', cadastroMateriais, name='cadastromateriais'),
    #path('materiais/cadastro/<int:id>', cadastroMateriais, name='cadastromateriais'),
    path('fornecedores', fornecedores, name='fornecedores'),
    path('fornecedores/cadastro/', cadastroFornecedor, name='cadastrofornecedores'),
    path('clientes', clientes, name='clientes'),
    path('clientes/cadastro/', cadastroClientes, name='cadastroclientes'),

    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('criarusuario', createUser, name='criarusuario'),

]

