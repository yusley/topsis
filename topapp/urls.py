from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),

    # MATERIAIS
    path('materiais', materiais, name='materiais'),
    path('materiais/cadastro/', cadastroMateriais, name='cadastromateriais'),
    path('materiais/cadastro/<int:id>', cadastroMateriais, name='editcadastromateriais'),
    
    # FORNECEDORES
    path('fornecedores', fornecedores, name='fornecedores'),
    path('fornecedores/cadastro/', cadastroFornecedor, name='cadastrofornecedores'),
    path('fornecedores/cadastro/<int:id>', cadastroFornecedor, name='editcadastrofornecedores'),
    
    # CLIENTES
    path('clientes', clientes, name='clientes'),
    path('clientes/cadastro/', cadastroClientes, name='cadastroclientes'),

    # USER
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('criarusuario', createUser, name='criarusuario'),

]

