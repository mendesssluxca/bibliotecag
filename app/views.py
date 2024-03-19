from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self,request):
        return render(request,'index.html',)
    def post(self,request):
        pass
class UsuarioView(View):
    def get(self,request):
        usuario = Usuario.objects.all()
        return render(request,'usuario.html',{'usuario': usuario})
    def post(self,request):
        pass
class GeneroView(View):
    def get(self,request):
        genero = Genero.objects.all()
        return render(request,'genero.html',{'genero': genero})
    def post(self,request):
        pass
class EditoraView(View):
    def get(self,request):
        editora = Editora.objects.all()
        return render(request,'editora.html',{'editora': editora})
    def post(self,request):
        pass
class AutorView(View):
    def get(self,request):
        autor = Autor.objects.all()
        return render(request,'autor.html',{'autor': autor})
    def post(self,request):
        pass
class LivroView(View):
    def get(self,request):
        livros = Livro.objects.all()
        return render(request,'livro.html',{'livros': livros})
    def post(self,request):
        pass
class EmprestimoView(View):
    def get(self,request):
        emprestimo = Emprestimo.objects.all()
        return render(request,'emprestimo.html',{'emprestimo': emprestimo})
    def post(self,request):
        pass
class CidadeView(View):
    def get(self,request):
        cidade = Cidade.objects.all()
        return render(request,'cidade.html',{'cidade': cidade})
    def post(self,request):
        pass
