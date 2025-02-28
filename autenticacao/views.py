from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastro (request):
    pessoa=[{'nome':'Caio Sampaio',
             'idade':'20',
             'profissao':'Escritor'},
             {'nome':'Thiago Martins',
             'idade':'30',
             'profissao':'Professor'}]
    

    return render(request,'index.html',{'pessoas':pessoa})