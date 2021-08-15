from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Task(models.Model):

    STATUS = (
        ('doing' , 'Doing'),
        ('done' , 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField( blank =True)
    foto = models.ImageField(upload_to="%Y/%m/%d/", null=True, blank=True)
    foto2 = models.ImageField(upload_to="%Y/%m/%d/", null=True, blank=True)
    foto3 = models.ImageField(upload_to="%Y/%m/%d/", null=True, blank=True)
    foto4 = models.ImageField(upload_to="%Y/%m/%d/", null=True, blank=True)
    done = models.CharField(
        max_length=5,
        choices= STATUS,
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):


    Nome = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Setor = models.CharField(max_length=255)
    Ramal = models.CharField(max_length=100, blank=True)
    Nascimento = models.CharField(max_length=100, null=True, blank=True,  help_text='Ex: Dia/Mês/Ano')

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nome

class Galeria(models.Model):

    title = models.CharField(max_length=255)
  
    description = models.TextField( blank =True)
    
    foto = models.ImageField(upload_to="galeria", null=False, blank=False)
    foto2 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto3 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto4 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto5 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto6 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto7 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto8 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto9 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto10 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto11 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto12 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto13 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto14 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto15 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto16 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto17 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto18 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto19 = models.ImageField(upload_to="galeria", null=True, blank=True)
    foto20 = models.ImageField(upload_to="galeria", null=True, blank=True)

    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Formularios_DB(models.Model):

    title = models.CharField(max_length=255)
  
    description = models.TextField( blank =True)
    
    foto = models.FileField(upload_to="formularios", null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
class Base_conhecimento(models.Model):

    title = models.CharField(max_length=255)
  
    description = models.TextField( blank =True)
    
    foto = models.FileField(upload_to="Base_conhecimentos", null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Sugestao(models.Model):

    Nome = models.CharField(max_length=255, blank =True)
    Descrição = models.TextField(blank = False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Descrição


