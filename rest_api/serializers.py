from rest_framework import serializers
from .models import Aluno, Motorista, Van

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'endereco', 'email', 'telefone', 'foto', 'van']


class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['nome', 'cnh', 'telefone', 'foto', 'usuario'  ]


class VanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Van
        fields = ['placa', 'modelo', 'vagas', 'horario', 'foto_van', 'motorista']