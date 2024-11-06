from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group


# Create your models here.



class Filial(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class CustomUser(AbstractUser):
    fk_filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=True)



class Fornecedor(models.Model):
    nome = models.CharField(max_length=255, null=False, )
    rua = models.CharField(max_length=255, null=False)
    bairro = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)


class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False)
    medida = models.CharField(max_length=255, null=False, )
    fk_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, )
    telefone = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    rua = models.CharField(max_length=255, null=False)
    bairro = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)
    numero = models.CharField(max_length=255, null=False)


class ProdutoCliente(models.Model):
    quantidade = models.CharField(max_length=255, null=False)
    valor = models.CharField(max_length=255, null=False)
    medida = models.CharField(max_length=255, null=False)
    fk_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=False)


class Patrimonio(models.Model):
    quantidade = models.CharField(max_length=255, blank=False, null=False)
    valor = models.CharField(max_length=255, blank=False, null=False)
    fk_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False)
    fk_filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=False)


class Orcamento(models.Model):
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    fk_produto_cliente = models.ForeignKey(ProdutoCliente, on_delete=models.CASCADE, null=False)
    fk_filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=False)


class Estoque(models.Model):
    quantidade = models.CharField(max_length=255, null=False, blank=False)
    quantidade_reservada = models.CharField(max_length=255, null=False, blank=False)
    fk_produto = models.ForeignKey(Produto,on_delete=models.CASCADE, blank=False)
    fk_filial = models.ForeignKey(Filial,on_delete=models.CASCADE, blank=False)


class Estoque(models.Model):
    quantidade = models.CharField(max_length=255, null=False, blank=False)
    tipomovimentacao = models.CharField(max_length=255, null=False, blank=False)
    fk_produto = models.ForeignKey(Produto,on_delete=models.CASCADE, blank=False)
    fk_filial = models.ForeignKey(Filial,on_delete=models.CASCADE, blank=False)
    fk_usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=False)

    

# class Perfil(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Filial = models.ForeignKey(Filial, on_delete=models.CASCADE)s

#     def __str__(self) -> str:
#         return self.usuario.username