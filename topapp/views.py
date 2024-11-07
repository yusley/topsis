from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#Create your views here.



def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request, 'partials/login.html')
    
    else:

        username = request.POST.get('user')
        password = request.POST.get('password')

        print(username,password)
        user = authenticate(request,username=username, password=password)

        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('Usuário não existe!')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)

    return redirect('/login')


def createUser(request):

    if request.method == 'GET':
        return render( request ,'partials/createUser.html')
    else:

        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        username = request.POST.get('user')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = authenticate(request,username=username, password=password)

        print(user)
        if user is not None:
            
            return HttpResponse('Usuário ja existe!')
        else:
            
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email, 
                                            first_name=first_name, 
                                            last_name=second_name)

            user.save()

            return redirect('/login')



@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login')
def materiais(request):
    return render(request, 'materiais.html')


@login_required(login_url='/login')
def cadastroMateriais(request,id=None):
    return render(request, 'cadastromateriais.html')


@login_required(login_url='/login')
def fornecedores(request):
    return render(request, 'fornecedores.html')


@login_required(login_url='/login')
def cadastroFornecedor(request,id=None):
    return render(request, 'cadastrofornecedor.html')

@login_required(login_url='/login')
def clientes(request):
    return render(request, 'clientes.html')


@login_required(login_url='/login')
def cadastroClientes(request,id=None):
    return render(request, 'cadastrocliente.html')