from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"
    def __str__(self):
            return self.nome

class Cidade(models.Model):
    nome= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural ="Cidades"
    
    def __str__(self):
        return f'{self.nome}'
    
class Usuario(models.Model):
    nome = models.CharField(max_length =100)
    cpf = models.CharField(max_length =15)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural ="Usuarios"
    
    def __str__(self):
        return f'{self.nome, self.cpf, self.email}'

class Genero(models.Model):
    nome = models.CharField(max_length =100)
    
    class Meta:
        verbose_name_plural ="Generos"
    
    def __str__(self):
        return f'{self.nome}'

class Editora(models.Model):
    nome = models.CharField(max_length =100)
    site = models.CharField(max_length =100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural ="Editoras"
    
    def __str__(self):
        return f'{self.nome, self.site, self.cidade}'
    
class Autor(models.Model):
    nome = models.CharField(max_length =100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural ="Autores"
    
    def __str__(self):
        return f'{self.nome, self.cidade}'
    
class Livro(models.Model):
    nome = models.CharField(max_length =100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    datapublicacao = models.DateField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="Livros"
    
    def __str__(self):
        return f'{self.nome, self.preco, self.datapublicacao, self.editora, self.genero, self.autor}'

class Emprestimo(models.Model):
    dataemprestimo = models.DateField()
    datadevolucao = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural ="Emprestimos"
    
    def __str__(self):
        return f'{self.dataemprestimo, self.datadevolucao, self.usuario, self.livro}'

    

