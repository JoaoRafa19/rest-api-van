from .models import Aluno, Van, Motorista
from rest_framework import viewsets
from .serializers import AlunoSerializer, VanSerializer, MotoristaSerializer



def main(request):
    return HttpResponse("ola mundo")

class VansViewSet(viewsets.ModelViewSet):
    queryset = Van.objects.all()
    serializer_class = VanSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
