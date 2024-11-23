from rest_framework import viewsets
from .models import Funcionario, Cliente
from .serializers import FuncionarioSerializer, ClienteSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny

class SuaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]


# Views para renderização de HTML
def funcionarios_view(request):
    return render(request, 'app_clinica/funcionarios.html')

def clientes_view(request):
    return render(request, 'app_clinica/clientes.html')

def index_view(request):
    return render(request, 'app_clinica/index.html')

# API ViewSets
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

