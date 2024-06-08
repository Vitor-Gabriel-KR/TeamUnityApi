from django.shortcuts import render
from .models import Funcionario

def index(request):
    # Consulta SQL para obter o funcionário com id igual a 1
    funcionario = Funcionario.objects.raw('SELECT * FROM funcionarios WHERE id = 1')[0]
    return render(request, 'index.html', {'funcionario': funcionario})



# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#    return render(request,'index.html')