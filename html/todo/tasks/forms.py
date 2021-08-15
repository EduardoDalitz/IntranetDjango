from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Task
from .models import Galeria
from .models import User
from .models import Formularios_DB
from .models import Sugestao


class TaskForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput, required = False)
    
    class Meta:
        
        model = Task
        fields = ('title','description', 'foto', 'foto2','foto3', 'foto4')

class GaleriaForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput, required = False)
    
    class Meta:
        
        model = Galeria
        fields = ('title','description', 'foto', 'foto2','foto3', 'foto4', 'foto5',
        'foto6','foto7','foto8','foto9','foto10','foto11','foto12','foto13','foto14',
        'foto15','foto16','foto17','foto18','foto19','foto20',)

class UserForm(forms.ModelForm):
    
    class Meta:
        
        model = User
        fields = ('Nome','Email', 'Setor', 'Ramal','Nascimento')
   

class Formularios_DBForm(forms.ModelForm):
    foto = forms.FileField(widget=ClearableFileInput, required = False)

    class Meta:
        
        model = Formularios_DB
        fields = ('title','description', 'foto')

class SugestaoForm(forms.ModelForm):
    
    class Meta:
        
        model = Sugestao
        fields = ('Nome','Descrição')
