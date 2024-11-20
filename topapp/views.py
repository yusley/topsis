from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
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

    if request.method == 'GET':

        materiais = Produto.objects.all()

        return render(request, 'materiais.html',{'materiais':materiais})
    else :

        pesquisa = request.POST.get('pesquisa')
        
        if pesquisa:
            materiais = Produto.objects.filter(nome__icontains=pesquisa)
        else:
            materiais = Produto.objects.all()

        return render(request, 'materiais.html',{'materiais':materiais})


@login_required(login_url='/login')
def cadastroMateriais(request,id=None):

    if request.method == 'GET':


        if id != None:
            material = Produto.objects.filter(id=id).first()
        else:
            material = None
        

        fornecedores = Fornecedor.objects.all()

        return render(request, 'cadastromateriais.html', {'fornecedores':fornecedores,'material':material})
       

    else :

        fornecedores = Fornecedor.objects.all()
        
        form = ProdutoForm(request.POST)


        if form.is_valid():

            if id != None:

                object = Produto.objects.filter(nome=form.cleaned_data['nome']).first()


                material = {
                    'nome':form.data['nome'],
                    'fk_fornecedor': form.data['fk_fornecedor'],
                    'unidadeMedida' : form.data['unidadeMedida'],
                    'medida': form.data['medida']
                }


                if object:
                    if object.nome == material['nome'] and object.id != id:
                        return render(request, 'cadastromateriais.html', {'fornecedores': fornecedores,'message':'Produto ja cadastrado!','tipo':'danger','material':material})
                
                material = Produto.objects.filter(id=id).first()

                material.nome = form.cleaned_data['nome']
                material.fk_fornecedor = form.cleaned_data['fk_fornecedor']
                material.unidadeMedida = form.cleaned_data['unidadeMedida']
                material.medida = form.cleaned_data['medida']

                material.save()

               
                return render(request, 'cadastromateriais.html', {'fornecedores':fornecedores,'message':'Salvo com sucesso!','tipo':'success','material':material})

            else:

                object = Produto.objects.filter(nome=form.cleaned_data['nome']).first()

                material = {
                    'nome':form.data['nome'],
                    'fk_fornecedor': form.data['fk_fornecedor'],
                    'unidadeMedida' : form.data['unidadeMedida'],
                    'medida': form.data['medida']
                }

                if object:
                    
                    return render(request,'cadastromateriais.html', {'fornecedores': fornecedores,'message':'Produto ja cadastrado!','tipo':'danger','material':material})
                
                material = form.save(commit=False)
                material.nome = form.cleaned_data['nome']
                material.fornecedor = form.cleaned_data['fk_fornecedor']
                material.unidadesMedida = form.cleaned_data['unidadeMedida']
                material.medida = form.cleaned_data['medida']
                
                material.save()

                return redirect('editcadastromateriais',id=material.id)
        else:

            return render(request, 'cadastromateriais.html', {'fornecedores':fornecedores,'message':'Erro nos dados!','tipo':'danger'})



@login_required(login_url='/login')
def fornecedores(request):

    fornecedores = Fornecedor.objects.all()

    return render(request, 'fornecedores.html', {'fornecedores':fornecedores})


@login_required(login_url='/login')
def cadastroFornecedor(request,id=None):

    if request.method == 'GET':

        if id != None:
            fornecedores = Fornecedor.objects.filter(id=id).first()
        else:
            fornecedores = None

        return render(request, 'cadastrofornecedor.html', {'fornecedores':fornecedores})
    else:
       
        form = FornecedorForm(request.POST)

        if form.is_valid():

            object = Fornecedor.objects.filter(nome=form.cleaned_data['nome']).first()

            if object:
                
                return render(request, 'cadastrofornecedor.html', {'message':'Fornecedor ja cadastrado!','tipo':'danger'})

            obj = form.save(commit=False)
            obj.descricao = form.cleaned_data['nome']
            obj.rua = form.cleaned_data['rua']
            obj.numero = form.cleaned_data['numero']
            obj.bairro = form.cleaned_data['bairro']
            obj.cidade = form.cleaned_data['cidade']
            obj.status = form.cleaned_data['status']

            obj.save()

            return render(request, 'cadastrofornecedor.html', {'message':'Salvo com sucesso!','tipo':'success'})
        
        else:
            print('erro')
            return render(request, 'cadastrofornecedor.html', {'message':'Erro nos dados!','tipo':'danger'})

        





@login_required(login_url='/login')
def clientes(request):
    return render(request, 'clientes.html')


@login_required(login_url='/login')
def cadastroClientes(request,id=None):
    return render(request, 'cadastrocliente.html')