# Comandos de Django
`README` com instruções da seção de Django do curso de Python do Otávio Miranda.

## Sobre o Django
Djando é uma framework web extremamente poderosa, podendo ser usada para criar sites ou até mesmo api. Irei destacar somente o essencial nesse `README`, pois é uma biblioteca imensa. Nesse arquivo Markdown será usado constantemente os arquivos nesse repositório como exemplo.

## Comandos básicos para inicio do projeto
No terminal, criar uma venv e instalar o Django com ```pip install django```, após isso, iniciar o projeto com o seguinte comando:
```
django-admin startproject <projectname> .
```
o `.` no final é para criar na raiz do projeto, pessoalmente prefiro, pois se torna mais simples mexer.


Para fazer o primeiro teste e subir seu projeto Django, execute:
```
python manage.py runserver
```

Qualquer dúvida usar o comando `python manage.py --help`

## Arquivos estáticos (static files) e templates
Antes de falarmos dos app no Django, temos que falar de templates e static files. 

Dentro de um projeto Django, é comum ter uma pasta chamada templates para armazenar os arquivos HTML dos templates e outra pasta chamada static para conter os arquivos estáticos como CSS, JavaScript, imagens, etc. Essas pastas são configuradas no projeto Django para que o framework possa localizá-las e utilizá-las conforme necessário ao renderizar páginas da web.

No caso desse projeto de demonstração, foi criado uma pasta base, lá está os templates e static files juntos, entretanto pode ser feito e até recomendo fazer separado, por exemplo:

```
base_static/global/css
base_templates/global/
```

Após criar as pastas, é necessário fazer o Django reconhecer esses caminhos em `project/settings.py`. Crie a constante `STATICFILES_DIRS` e adicione o template em `DIRS` na constante `TEMPLATES`:
```
STATICFILES_DIRS = (BASE_DIR / 'base_static',)
```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base_templates'
        ],
```

## Criando, configurando e usando apps no Django
Da para resumir apps Django como páginas do seu site ou api, dependendo do seu objetivo. Por exemplo, criar um app com nome `home` para a página inicial do seu site, mas se tiver outra página totalmente diferente, recomendado criar outro app, como por exemplo o app `blog` que está nesses arquivos do projeto.

Para a criação do app, executar o seguinte comando:
```
python manage.py startapp <appname>
```

Com o app criado, você deve configurar para o Django reconhecer. Na constante `INSTALLED_APPS` em `project/settings.py`, você deve por o nome do seu app, por exemplo o app `home`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]
```

Outra configuração em `project` é no arquivo `urls.py`, onde deve ser adicionado o caminho das urls de seu app:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
```
Na função `path()`, o primeiro parametro é a url do app, no caso está vazia pois será a página inicial, entretanto, se tivesse outro app, poderia por outra url como `blog/`. No segundo parametro deve-se usar o `include` para o caminho do arquivo de urls do app, no caso é `home/urls.py`.

Crie o arquivo `urls.py` na pasta do aplicativo, será colocado a url pertecente a cada view desse respectivo app:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

```

Dentro da pasta do seu app, crie uma pasta de template, aconselhado criar outra pasta com o nome do seu app e dentro criar um arquivo `index.html`, onde será a página do seu app, após isso configurar o caminho no arquivo `views.py`, como no exemplo seguinte:
```
home/template/home/intex.html
```

Dentro de `views.py` do app `home`:
```
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')
```