from django.shortcuts import render
from django.http import HttpResponse, request

# V2
def home(request):
    return render(request, 'home.html', {'nome': 'Alexandre'})


# V1
# def home(requests):
#     return HttpResponse('Olá')
