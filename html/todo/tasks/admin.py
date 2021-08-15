from django.contrib import admin

from django.core.management.commands.runserver import Command as runserver
runserver.default_port = "80"
# Register your models here.
from .models import Task
from .models import User
from .models import Galeria
from .models import Formularios_DB
from .models import Base_conhecimento
from .models import Sugestao



admin.site.register(Task)
admin.site.register(User)
admin.site.register(Galeria)
admin.site.register(Formularios_DB)
admin.site.register(Base_conhecimento)
admin.site.register(Sugestao)

