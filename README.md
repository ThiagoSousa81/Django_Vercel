[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

# Django + Vercel

Este exemplo mostra como usar Django 4 no Vercel com Serverless Functions usando o [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://django-template.vercel.app/

## Como funciona

Nosso aplicativo Django, `example` está configurado como um aplicativo instalado em `vercel_app/settings.py`:

```python
# vercel_app/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

Nós permitimos "\*.vercel.app" subdomínios em `ALLOWED_HOSTS`, além de 127.0.0.1:

```python
# vercel_app/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

O módulo `wsgi` deve usar uma variável pública chamada `app` para expor a aplicação WSGI:

```python
# vercel_app/wsgi.py
app = get_wsgi_application()
```

A configuração `WSGI_APPLICATION` correspondente é configurada para usar a variável `app` do módulo `vercel_app.wsgi`:

```python
# vercel_app/settings.py
WSGI_APPLICATION = 'vercel_app.wsgi.app'
```

Existe uma única visualização que renderiza a hora atual em `example/views.py`:

```python
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
```

Esta visualização é exposta em um URL por meio de `example/urls.py`:

```python
# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index),
]
```

Finalmente, ele fica acessível ao servidor Django dentro de `vercel_app/urls.py`:

```python
# vercel_app/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

Este exemplo usa o Web Server Gateway Interface (WSGI) com Django para permitir o tratamento de solicitações no Vercel com funções sem servidor.

## Executando localmente

```bash
python manage.py runserver
```

Sua aplicação Django agora está disponível em `http://localhost:8000`.

## Implantação com um clique

Implante o exemplo usando [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Vercel&demo-description=Use%20Django%204%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)
