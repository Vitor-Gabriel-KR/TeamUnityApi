from django.shortcuts import render
from .models import Funcionario

def index(request):
    id_to_search = 2
    funcionario = Funcionario.objects.raw('SELECT * FROM funcionarios WHERE id = %s', [id_to_search])[0]
    return render(request, 'index.html', {'funcionario': funcionario})



# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#    return render(request,'index.html')