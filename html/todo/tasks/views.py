from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import date
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import logging, traceback


from .forms import TaskForm
from .forms import GaleriaForm
from .forms import UserForm
from .forms import Formularios_DBForm
from .forms import SugestaoForm

from .models import Task
from .models import User
from .models import Galeria
from .models import Formularios_DB
from .models import Base_conhecimento
from .models import Sugestao

logger = logging.getLogger('django')

@login_required
def alterarSenha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, 'Senha Alterada!')
            logger.info('Funcao: Senha alterada => Nome do usuario: {} '.format(request.user))
            return render(request, "alterarSenha.html")
            
        else:
            messages.info(request, 'Erro na alteração da Senha!')
            logger.info('Funcao: Erro na alteracao da senha => Nome do usuario: {} '.format(request.user))
            return redirect("alterarSenha.html")
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form' : form
        } 
    return render(request, "alterarSenha.html", context)

def TaskGaleria(request):
    search = request.GET.get('search')

    if search:
        tasks = Galeria.objects.filter(title__icontains=title)
        logger.info('Funcao: if / TaskGaleria => Nome do usuario: {} '.format(request.user))
    else:

        tasks_list = Galeria.objects.all().order_by('title')

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)
        logger.info('Funcao: else / TaskGaleria => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/galeria_fotos.html', {'tasks': tasks})


def TaskFormularios(request):
    search = request.GET.get('search')

    if search:
     
        tasks = Formularios_DB.objects.filter(title__icontains=title)
        logger.info('Funcao: if / TaskFormularios => Nome do usuario: {} '.format(request.user))
    else:

        tasks_list = Formularios_DB.objects.all().order_by('title')

        paginator = Paginator(tasks_list, 10)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)
        logger.info('Funcao: else / TaskFormularios => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/departamentos/formularios.html', {'tasks': tasks})


def TaskBase_conhecimento(request):
    search = request.GET.get('search')

    if search:
     
        tasks = Base_conhecimento.objects.filter(title__icontains=title)
        logger.info('Funcao: if / TaskBase_conhecimento => Nome do usuario: {} '.format(request.user))
    else:

        tasks_list = Base_conhecimento.objects.all().order_by('title')

        paginator = Paginator(tasks_list, 10)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

        logger.info('Funcao: else / TaskBase_conhecimento => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/departamentos/base_conhecimento.html', {'tasks': tasks})

@login_required
def users(request):
    search = request.GET.get('search')

    if search:
        tasks = User.objects.filter(Nome__icontains=search, usuario=request.user)
        logger.info('Funcao: if / users => Nome do usuario: {} '.format(request.user))

    else:

        tasks_list = User.objects.all().order_by('-created_at').filter(usuario=request.user)

        paginator = Paginator(tasks_list, 10)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

        logger.info('Funcao: else / users => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/users.html', {'tasks': tasks})

def TaskListusers(request):
    search = request.GET.get('search')

    if search:
        tasks = User.objects.filter(Nome__icontains=search)
        logger.info('Funcao: if / TaskListusers => Nome do usuario: {} '.format(request.user))
    else:

        tasks_list = User.objects.all().order_by('Nome')

        paginator = Paginator(tasks_list, 100)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

        logger.info('Funcao: else / TaskListusers => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/comunicacao/emails_brascola.html', {'tasks': tasks})


def TaskListusersEmail(request):
    search = request.GET.get('search')

    if search:
        tasks = User.objects.filter(Nome__icontains=search)
        logger.info('Funcao: if / TaskListusersEmail => Nome do usuario: {} '.format(request.user))

    else:

        tasks_list = User.objects.all().order_by('Setor')

        paginator = Paginator(tasks_list, 100)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

        logger.info('Funcao: else / TaskListusersEmail => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/comunicacao/ramais_brascola.html', {'tasks': tasks})

def TaskListfeed(request):
    search = request.GET.get('search')

    from datetime import date, datetime
    import time  
    
    logger.info('Funcao: TaskListfeed => Nome do usuario: {} '.format(request.user))
    today = date.today()
    data =today.strftime("%d/%m")
    print(data)
    
    nasc = User.objects.filter(Nascimento__icontains=data)

    vetor = []
    
    for x in range(0, len(nasc)):
        vetor.append(str(nasc[x]))
    
    print(vetor)
    #print(request.user.get_all_permissions())


    if search:

        tasks = Task.objects.filter(title__icontains=search)
        logger.info('Funcao: if / TaskListfeed => Nome do usuario: {} '.format(request.user))

    else:

        tasks_list = Task.objects.all().order_by('-created_at')

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')
        
        tasks = paginator.get_page(page)

        usuario = request.user

        logger.info('Funcao: else / TaskListfeed => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/index.html', {'tasks': tasks, 'today': today, 'vetor':vetor})

@login_required
def TaskList(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, usuario=request.user)

        logger.info('Funcao: if / TaskList => Nome do usuario: {} '.format(request.user))

    else:

        tasks_list = Task.objects.all().order_by('-created_at').filter(usuario=request.user)

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)
        logger.info('Funcao: else / TaskList => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/teste.html', {'tasks': tasks})

@login_required

def editgaleria(request):
    search = request.GET.get('search')

    if search:
        tasks = Galeria.objects.filter(title__icontains=search, usuario=request.user)

        logger.info('Funcao: if / editgaleria => Nome do usuario: {} '.format(request.user))

    else:

        tasks_list = Galeria.objects.all().order_by('-created_at').filter(usuario=request.user)

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

        logger.info('Funcao: else / editgaleria => Nome do usuario: {} '.format(request.user))

    return render(request, 'tasks/galeria.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    logger.info('Funcao: taskView => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/task.html', {'task': task})

def taskViewGaleria(request, id):
    task = get_object_or_404(Galeria, pk=id)
    logger.info('Funcao: taskViewGaleria => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/taskGaleria.html', {'task': task})

def taskViewUser(request, id):
    task = get_object_or_404(User, pk=id)
    logger.info('Funcao: taskViewUser => Nome do usuario: {} '.format(request.user))
    return render(request, 'tasks/taskUser.html', {'task': task})


@login_required
@permission_required('tasks.add_task', raise_exception=True)
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        logger.info('Funcao: if / newTask => Nome do usuario: {} '.format(request.user))

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.usuario = request.user
            task.save()
            logger.info('Funcao: if form.is_valid() / newTask => Nome do usuario: {} '.format(request.user))
            return redirect('/teste.html')
    
    else:
        form = TaskForm()
        logger.info('Funcao: else / newTask => Nome do usuario: {} '.format(request.user))
        return render(request, 'tasks/addtask.html', {'form':form})


@login_required
@permission_required('tasks.add_galeria', raise_exception=True)
def newGaleria(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        logger.info('Funcao: if / newGaleria => Nome do usuario: {} '.format(request.user))

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.usuario = request.user
            task.save()
            logger.info('Funcao: if form.is.valid() / newGaleria => Nome do usuario: {} '.format(request.user))
            return redirect('/galeria.html')
        
    
    else:
        form = GaleriaForm()
        logger.info('Funcao: else / newGaleria => Nome do usuario: {} '.format(request.user))
        return render(request, 'tasks/addgaleria.html', {'form':form})
        
@login_required
@permission_required('tasks.add_user', raise_exception=True)
def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        logger.info('Funcao: if / newUser => Nome do usuario: {} '.format(request.user))

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.usuario = request.user
            task.save()
            logger.info('Funcao: if form.is.valid / newUser => Nome do usuario: {} '.format(request.user))
            return redirect('/users.html')
    
    else:
        form = UserForm()
        logger.info('Funcao: else / newUser => Nome do usuario: {} '.format(request.user))

        return render(request, 'tasks/addUser.html', {'form':form})


def newSugestao(request):  
    if request.method == 'POST':
        form = SugestaoForm(request.POST, request.FILES)
        logger.info('Funcao: if / newSugestao => Nome do usuario: - ')

        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.info(request, 'Sugestão enviada com sucesso!')
            logger.info('Funcao: if form.is.valid / newSugestao => Nome do usuario: - ')
            return redirect('/')
    else:
        form = SugestaoForm()
        logger.info('Funcao: else / NewSugestao => Nome do usuario: - ')
        return render(request, 'tasks/addSugestao.html', {'form':form})


@login_required
@permission_required('tasks.change_task', raise_exception=True)
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    
    if(request.method == 'POST'):
        form = TaskForm(request.POST, request.FILES, instance=task)
        logger.info('Funcao: if / editTask => Nome do usuario: {} '.format(request.user))

        if(form.is_valid()):
            if (task.usuario == request.user):
                task.save()
                logger.info('Funcao: if > if form.is.valid > if / editTask => Nome do usuario: {} '.format(request.user))
                return redirect('/teste.html')
            else: 
                logger.info('Funcao: if > if form.is.valid > else / editTask => Nome do usuario: {} '.format(request.user))
                return redirect('/')

        else:
            logger.info('Funcao: if form.is.valid() > else / editTask => Nome do usuario: {} '.format(request.user))
            return render(request, 'tasks/edittask.html', {'form':form, 'task':task})    

    else:
        logger.info('Funcao: else / editTask => Nome do usuario: {} '.format(request.user))
        return render(request, 'tasks/edittask.html', {'form':form, 'task':task})

@login_required
@permission_required('tasks.change_user', raise_exception=True)
def editUser(request, id):
    task = get_object_or_404(User, pk=id)
    form = UserForm(instance=task)
    logger.info('Funcao: editUser => Nome do usuario: {} '.format(request.user))

    if(request.method == 'POST'):
        form = UserForm(request.POST, request.FILES, instance=task)
        logger.info('Funcao: if / editUser => Nome do usuario: {} '.format(request.user))

        if(form.is_valid()):
            if (task.usuario == request.user):
                task.save()
                logger.info('Funcao: if > if > if / editUser => Nome do usuario: {} '.format(request.user))
                return redirect('/users.html')
            else: 
                logger.info('Funcao: if > if > else / editUser => Nome do usuario: {} '.format(request.user))
                return redirect('/')

        else:
            logger.info('Funcao: if > else / editUser => Nome do usuario: {} '.format(request.user))
            return render(request, 'tasks/editUser.html', {'form':form, 'task':task})    

    else:
        logger.info('Funcao: else / editUser => Nome do usuario: {} '.format(request.user))
        return render(request, 'tasks/editUser.html', {'form':form, 'task':task})

@login_required
@permission_required('tasks.change_galeria', raise_exception=True)
def editGaleria(request, id):
    task = get_object_or_404(Galeria, pk=id)
    form = GaleriaForm(instance=task)
    logger.info('Funcao: editGaleria => Nome do usuario: {} '.format(request.user))

    if(request.method == 'POST'):
        form = GaleriaForm(request.POST, request.FILES, instance=task)
        logger.info('Funcao: if / editGaleria => Nome do usuario: {} '.format(request.user))

        if(form.is_valid()):
            if (task.usuario == request.user):
                task.save()
                logger.info('Funcao: if > if > if / editGaleria => Nome do usuario: {} '.format(request.user))
                return redirect('/galeria.html')
            else: 
                logger.info('Funcao: if > if > else / editGaleria => Nome do usuario: {} '.format(request.user))
                return redirect('/')

        else:
            logger.info('Funcao: if > else / editGaleria => Nome do usuario: {} '.format(request.user))
            return render(request, 'tasks/editGaleria.html', {'form':form, 'task':task})    

    else:
        logger.info('Funcao: else / editGaleria => Nome do usuario: {} '.format(request.user))
        return render(request, 'tasks/editGaleria.html', {'form':form, 'task':task})

@login_required
@permission_required('tasks.delete_task', raise_exception=True)
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Notícia deletada!')
    logger.info('Funcao: deleteTask => Nome do usuario: {} '.format(request.user))
    return redirect('/teste.html')

@login_required
@permission_required('tasks.delete_user', raise_exception=True)
def deleteUser(request, id):
    task = get_object_or_404(User, pk=id)
    task.delete()
    logger.info('Funcao: deleteUser => Nome do usuario: {} '.format(request.user))

    return redirect('/users.html')

@login_required
@permission_required('tasks.delete_galeria', raise_exception=True)
def deleteGaleria(request, id):
    task = get_object_or_404(Galeria, pk=id)
    task.delete()

    logger.info('Funcao: deleteGaleria => Nome do usuario: {} '.format(request.user))

    return redirect('/galeria.html')

@login_required
def teste(request):
    return render(request, 'tasks/teste.html')

@login_required
def feed(request):
    return render(request, 'tasks/feed.html')

def helloWorld(request):
    ano_atual = date.today().year
    mes_atual = date.today().month
    dia_atual = date.today().day

    dia_bras = 25
    mes_bras = 9
    ano_bras = 1953
    if dia_bras >= dia_atual:
        if mes_bras >= mes_atual:
            idade = ano_atual - ano_bras


    return HttpResponse(idade)
    
def diretoria(request):
    return render(request, 'tasks/diretoria.html')   
    
def index(request):
    return render(request, 'tasks/index.html')

def apresentacao(request):
    return render(request, 'tasks/apresentacao.html')

def historia(request):
    return render(request, 'tasks/historia.html')

def diretoria(request):
    return render(request, 'tasks/diretoria.html')   
    
def departamentos(request):
    return render(request, 'tasks/departamentos.html')

def app(request):
    return render(request, 'tasks/app.html')

def ramais(request):
    return render(request, 'tasks/comunicacao/ramais_brascola.html')

def emails(request):
    return render(request, 'tasks/comunicacao/emails_brascola.html')

def adm_vendas(request):
    return render(request, 'tasks/departamentos/adm_vendas.html')

def assistencia_tecnica(request):
    return render(request, 'tasks/departamentos/assistencia_tecnica.html')

def cq(request):
    return render(request, 'tasks/departamentos/cq.html')

def gestao_da_qualidade(request):
    return render(request, 'tasks/departamentos/gestao_da_qualidade.html')

def marketing(request):
    return render(request, 'tasks/departamentos/marketing.html')

def rh(request):
    return render(request, 'tasks/departamentos/rh.html')

def seguranca_do_trabalho(request):
    return render(request, 'tasks/departamentos/seguranca_do_trabalho.html')

def ti(request):
    return render(request, 'tasks/departamentos/ti.html')

def vendas_internas(request):
    return render(request, 'tasks/departamentos/vendas_internas.html')

def politicas_de_acesso(request):
    return render(request, 'tasks/comunicados/politicas_de_acesso.html')

def dica_saude_covid19(request):
    return render(request, 'tasks/comunicados/dica_saude_covid19.html')

def galeria_fotos(request):
    return render(request, 'tasks/galeria_fotos.html')

def sipat_2019(request):
    return render(request, 'tasks/_multimidia/_sipat_2019/sipat_2019.html')

def aniversario_brascola_66_anos(request):
    return render(request, 'tasks/_multimidia/_aniversario_brascola_66_anos/aniversario_brascola_66_anos.html')

def final_de_ano_2019(request):
    return render(request, 'tasks/_multimidia/_final_de_ano_2019/final_de_ano_2019.html')

def gerencia(request):
    return render(request, 'tasks/departamentos/gerencias.html')

def juridico(request):
    return render(request, 'tasks/departamentos/juridico.html')

def producao(request):
    return render(request, 'tasks/departamentos/producao.html')

def secretaria(request):
    return render(request, 'tasks/departamentos/secretaria.html')

def suprimentos(request):
    return render(request, 'tasks/departamentos/suprimentos.html')

def comunicacoes(request):
    return render(request, 'tasks/departamentos/comunicacoes.html')

