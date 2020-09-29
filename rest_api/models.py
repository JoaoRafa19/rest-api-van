from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Motorista(models.Model):
    nome = models.CharField(max_length=50)
    cnh = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    foto = models.ImageField(upload_to='Motoristas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Motoristas'


class Van(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=20)
    vagas = models.IntegerField(null=True, blank=True)
    horario = models.DateTimeField(blank=True, null=True)
    foto_van = models.ImageField(upload_to='Vans')
    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT)

    class Meta:
        db_table = 'Vans'

    def __str__(self):

        return self.placa+self.modelo

class Aluno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=7)
    endereco = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    foto = models.ImageField(upload_to='alunos')
    van = models.ForeignKey(Van,on_delete=models.PROTECT, blank=True, default=None, null=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Alunos'
        


    
    
