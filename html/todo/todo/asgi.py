"""
ASGI config for todo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

application = get_asgi_application()

#WSGI (significa Web Server Gateway Interface) é simples, onde você pode 
# definir seu aplicativo como um objeto que leva dois argumentos o primeiro argumento 
# Environment descreve a solicitação e o ambiente em que o servidor está sendo executado e o segundo argumento é um objeto
#  síncrono que você chama comece a resposta para ceder o corpo.

# ASGI Asynchronous Server Gateway Interface, fica como se fosse atualizando os dados o tempo todo, gerando trafego na rede.