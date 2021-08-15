from django.urls import path

from . import views 

urlpatterns = [
    
    path('alterarSenha.html', views.alterarSenha, name='alterarSenha'),
    path('teste.html', views.TaskList, name='task_list'),

    path('galeria.html', views.editgaleria, name='task_list'),

    path('users.html', views.users, name='task_list'),

    path('emails_brascola.html', views.TaskListusers, name='task_list'),
    path('ramais_brascola.html', views.TaskListusersEmail, name='task_list'),

    path('galeria_fotos.html', views.TaskGaleria, name='task_list'),

    path('formularios.html', views.TaskFormularios, name='task_list'),
    path('base_conhecimento.html', views.TaskBase_conhecimento, name='task_list'),

    path('task/<int:id>', views.taskView, name='task-view'),
    path('taskGaleria/<int:id>', views.taskViewGaleria, name='task-view'),
    path('taskUser/<int:id>', views.taskViewUser, name='task-view'),

    path('newtask/', views.newTask, name='new-task'),
    path('newGaleria/', views.newGaleria, name='new-task'),
    path('newUser/', views.newUser, name='new-task'),
    path('newSugestao/', views.newSugestao, name='new-Sugestao'),
     
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('editUser/<int:id>', views.editUser, name='edit-task'),
    path('editGaleria/<int:id>', views.editGaleria, name='edit-task'),

    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('deleteUser/<int:id>', views.deleteUser, name='delete-task'),
    path('deleteGaleria/<int:id>', views.deleteGaleria, name='delete-galeria'),
    #path('', views.index),
    path('', views.TaskListfeed, name='task_list'),
    path('feed.html', views.feed, name='task_list'),
    path('feed.html', views.feed),
    path('apresentacao.html', views.apresentacao),
    path('historia.html', views.historia),
    path('diretoria.html', views.diretoria),
    path('departamentos.html', views.departamentos),
    path('app.html', views.app),
    path('ramais_brascola.html', views.ramais),
    path('emails_brascola.html', views.emails),
    path('adm_vendas.html', views.adm_vendas),
    path('assistencia_tecnica.html', views.assistencia_tecnica),
    path('cq.html', views.cq),
    path('gestao_da_qualidade.html', views.gestao_da_qualidade),
    path('marketing.html', views.marketing),
    path('rh.html', views.rh),
    path('seguranca_do_trabalho.html', views.seguranca_do_trabalho),
    path('ti.html', views.ti),
    path('vendas_internas.html', views.vendas_internas),
    path('politicas_de_acesso.html', views.politicas_de_acesso),
    path('dica_saude_covid19.html', views.dica_saude_covid19),
    path('galeria_fotos.html', views.galeria_fotos),
    path('tasks/_multimidia/_sipat_2019/sipat_2019.html', views.sipat_2019),
    path('tasks/_multimidia/_aniversario_brascola_66_anos/aniversario_brascola_66_anos.html', views.aniversario_brascola_66_anos),
    path('tasks/_multimidia/_final_de_ano_2019/final_de_ano_2019.html', views.final_de_ano_2019),
    path('gerencias.html', views.gerencia),
    path('juridico.html', views.juridico),
    path('producao.html', views.producao),
    path('secretaria.html', views.secretaria),
    path('suprimentos.html', views.suprimentos),
    path('comunicacoes.html', views.comunicacoes),
    
    #path('teste.html', views.teste),

]
