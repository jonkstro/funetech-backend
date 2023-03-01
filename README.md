## BACKEND

### 01 - Criando o Projeto Django

- [x]  Instalar python mais atual;
- [x]  Criar pasta backend;
- [x]  Criar ambiente virtual: Digitar no cmd: `python -m venv .venv` e depois ativar ela: `.venv/Scripts/activate` (Windows);
- [ ]  Criar ambiente virtual: Digitar no cmd: `python -m venv .venv` e depois ativar ela: `source .venv/bin/activate` (Linux);
- [x]  Instalar Django: `pip install django`;
- [x]  (Caso vá trabalhar com imagens)Instalar Pillow: `pip install pillow` ;
- [x]  Configurar o arquivo ***settings.py :***
    - [x]  Alterar a lingua e timezone
        
        `LANGUAGE_CODE = 'pt-BR'`
        
        `TIME_ZONE = 'America/Fortaleza'`
        
    - [x]  Configurar os diretórios de imagens. Adicionar abaixo de `STATIC_URL = ‘static/’` :
        
        ```python
        # Definindo as pastas de imagens
        MEDIA_ROOT = 'imagens'
        MEDIA_URL = '/media/'
        ```
        
    - [x]  Configurar as definições de email (Caso precise enviar email para autenticação)
    - `Código`
        
        ```
        # Configurações do email server
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = 'djangophb@gmail.com'
        EMAIL_HOST_PASSWORD = 'vralergubbqdumbo'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        DEFAULT_FROM_EMAIL = 'djangophb@gmail.com'
        PROTOCOL = "http"
        DOMAIN = "127.0.0.1:8000"
        SITE_NAME = 'Funetech'
        ```
        
- [x]  Iniciar os repositórios git nas pastas: `git init`;
- [x]  Criar projeto: `django-admin startproject funetech .` ;
    - [x]  Rodar o projeto: `python manage.py runserver` ;

### 02 - Integrando com Django Rest Framework

- [x]  Digitar no cmd: `pip install djangorestframework`;
- [x]  Adicionar em installed apps no settings: `‘rest_framework’,` ;
- [x]  Fazer as migrações: `python manage.py migrate`;
- [x]  Criar o usuário admin: `python manage.py createsuperuser` ;
- [x]  Criar arquivo **s**************erializers.py**************** dentro da pasta do projeto ************************funetech***************** e adicionar a configuração abaixo:
- `Código`:
    
    ```python
    from django.contrib.auth.models import User
    from rest_framework import serializers
    from django.contrib.auth.hashers import make_password
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    class UserCreateSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True, required=True)
        username = serializers.CharField(write_only=True, required=False)
        class Meta:
            model = User
            fields = ['id', 'username', 'email', 'password', 'first_name', 'is_active']
        
        
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data.get('password'))
            validated_data['is_active'] = False
            validated_data['username'] = validated_data['email']
    
            return super(UserCreateSerializer, self).create(validated_data)
    ```
    
- [x]  Criar arquivo ***************************views.py*************************** na pasta do projeto ************************funetech************************ com a configuração abaixo:
- `Código`:
    
    ```python
    from rest_framework.response import Response
    from rest_framework.views import APIView
    
    import requests
    
    # REALIZAR A ATIVAÇÃO DA CONTA APÓS CLICAR NO LINK DO DJOSER
    class UserActivationView(APIView):
        def get (self, request, uid, token):
            protocol = 'https://' if request.is_secure() else 'http://'
            web_url = protocol + request.get_host()
            post_url = web_url + "/auth/users/activation/"
            post_data = {'uid': uid, 'token': token}
            result = requests.post(post_url, data = post_data)
            content = result.text
            return Response(content)
    ```
    
- Configurar o arquivo ***urls.py*** com a configuração abaixo :
    
    ```python
    from django.urls import include, path
    from rest_framework import routers
    from django.contrib import admin
    from funetech.views import UserActivationView
    
    from homenagem.views import HomenagemViewSet
    
    # importações para trabalhar com imagens
    from django.conf import settings
    from django.conf.urls.static import static
    
    router = routers.DefaultRouter()
    # SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
    router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
        path('auth/', include('djoser.urls')),
        # path('auth/', include('djoser.urls.jwt')),
        path('auth/', include('djoser.urls.authtoken')),
        # path('auth/', include('djoser.social.urls')),
        path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens
    ```
    
- [x]  Testar a api se funcionou: `python manage.py runserver`;
- [x]  Configurar grupos de usuários no localhost/admin ;

### 03 - Preparando ambiente GIT:

- [x]  Digitar comando `git init`;
- [x]  Criar arquivo ******************************.gitignore******************************;
    - [x]  Configurar o gitignore com o código abaixo pra ele excluir do github o ***venv e db***: (Colocar o nome da venv que você criou, ex: ‘.venv’, ‘venv1’, etc… );
        
        ```python
        .venv
        db.sqlite3
        ```
        
- [x]  Digitar no terminal: `pip freeze > requirements.txt` para preencher o arquivo com os programas instalados na venv (*Precisa estar com a venv ativada!!*)
- [x]  Digitar `git status` e checar se sumiu os arquivos do .***gitignore***
- [x]  Digitar `git add .` e depois `git commit -m "Primeiro commit, preparando o projeto."`
- [ ]  Digitar `git remote add origin [link do repositório do github]` ;
- [ ]  Digitar `git checkout -b main` para mudar o branch de master que vem por padrão para main que é o que está no github;
- [ ]  Digitar `git push -u origin main` para subir o programa pro github.

### 04 - Modelando a aplicação e criando os models

- [x]  Desenhar a hierarquia do sistema, para facilitar a modelagem do mesmo;
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a494f53c-f5da-4ccd-8f1d-244be0bc3269/Untitled.png)
    
- [x]  Digitar `python manage.py startapp homenagem` para criar as aplicações do sistema
- [x]  Adicionar em ************************************settings.py************************************  `‘homenagem’,` ;
- [x]  Configurar dentro do app criado o arquivo ***models.py***, nesse curso será usado lista de compras.
- `Código:`
    
    ```python
    from django.db import models
    from django.contrib.auth.models import User
    
    class Homenagem(models.Model):
        user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        nome = models.CharField(max_length=50, null=False, blank=False)
        data_nasc = models.DateField(null=False, blank=False)
        cidade_nasc = models.CharField(max_length=50, null=False, blank=False)
        data_falec = models.DateField(null=False, blank=False)
        cidade_falec = models.CharField(max_length=50, null=False, blank=False)
        memoria = models.TextField(max_length=255, null=True, blank=True)
        biografia = models.TextField(max_length=800, null=True, blank=True)
        biografia = models.TextField(max_length=800, null=True, blank=True)
        foto = models.ImageField(upload_to='homenagem', null=True, blank=True)
        created = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.nome
    ```
    
- [x]  Digitar `python manage.py makemigrations` e `python manage.py migrate` ;
- [x]  Adicionar a model no arquivo ***************************admin.py*************************** para registrar ele no /admin. Nesse projeto foi usado o código abaixo para sua configuração
- `Código:`
    
    ```python
    from django.contrib import admin
    from .models import List
    
    admin.site.register(List)
    ```
    

### 05 - Criando endpoint de homenagem

- [x]  Criar arquivo *********************************************serializers.py********************************************* na aplicação criada:
- Configuração do arquivo ***serializer.py*** ficou conforme abaixo:
    
    ```python
    from rest_framework import serializers
    from .models import Homenagem
    
    class HomenagemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Homenagem
            fields = ['id','name', 'user']
    ```
    
- Configuração do arquivo ***************************views.py*************************** ficou conforme abaixo:
    
    ```python
    from rest_framework import viewsets
    from rest_framework import permissions, authentication
    
    from .models import Homenagem
    from .serializers import HomenagemSerializer
    
    class HomenagemViewSet(viewsets.ModelViewSet):
        serializer_class = HomenagemSerializer
    
        # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
        permission_classes = [permissions.IsAuthenticated]
        authentication_classes = [
                authentication.TokenAuthentication, 
                authentication.SessionAuthentication
            ]
        # SERÁ MOSTRADO SOMENTE AS LISTAS DO USUÁRIO QUE TIVER LOGADO
        def get_queryset(self):
            user = self.request.user
            return Homenagem.objects.filter(user=user)
    ```
    
- [x]  Configurar o arquivo de ************************urls.py************************ do projeto principal
    - Configuração do arquivo ***************************urls.py*************************** ficou conforme abaixo:
        
        ```python
        from django.urls import include, path
        from rest_framework import routers
        from django.contrib import admin
        from funetech.views import UserActivationView
        
        from homenagem.views import HomenagemViewSet
        
        # importações para trabalhar com imagens
        from django.conf import settings
        from django.conf.urls.static import static
        
        router = routers.DefaultRouter()
        # SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
        router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include(router.urls)),
            path('auth/', include('djoser.urls')),
            # path('auth/', include('djoser.urls.jwt')),
            path('auth/', include('djoser.urls.authtoken')),
            # path('auth/', include('djoser.social.urls')),
            path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens
        ```
        
- RESULTADO DO JSON:
    
    ```json
    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/groups/1/",
            "name": "user"
        },
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/groups/2/",
            "name": "admin"
        }
    ]
    ```
    

### 06 - Ativando Sistema de TOKEN

- [x]  Adicionar nos apps instalados no ************************************settings.py************************************ : `'rest_framework.authtoken',` ;
- [x]  Adicionar em ***settings.py***  a configuração de exibição de views por Token
- `Código:`
    
    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            # 'api.authentication.TokenAuthentication',
            # 'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            # 'rest_framework_simplejwt.authentication.JWTAuthentication'
        ),
    }
    ```
    
- [x]  Realizar as migrações: `python manage.py makemigrations` e `python manage.py migrate` ;
- [x]  Rodar o servidor e testar se subiu o campo de Tokens: `python manage.py runserver`
- [ ]  Testar os endpoints no Postman com seus devidos tokens, conforme abaixo:
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aba726e9-7307-4472-bd0f-5abca12601d3/Untitled.png)
    
- [ ]  Adicionar os campos abaixo nas ***viewsets***, para só exibir as mesmas após autenticadas:
    
    ```python
    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
        permission_classes = [permissions.IsAuthenticated]
        authentication_classes = [
                    authentication.TokenAuthentication, 
                    authentication.SessionAuthentication
                ]
    ```
    
    ### 07 - Configurando o CORS do Django
    
    - [x]  Digitar: `pip install django-cors-headers` ;
    - [x]  Adicionar em **settings.py `'**corsheaders',`  aos installed apps;
    - [x]  Adicionar em ************************settings.py************************ `'corsheaders.middleware.CorsMiddleware',` , abaixo do *SessionMiddleware*  e acima do *CommonMiddleware*
    - [x]  Adicionar ao final do código os links que poderão acessar o servidor:
        
        ```python
        # Configurar os endereços que poderão acessar ao servidor
        CORS_ALLOWED_ORIGINS = [
            # "https://example.com",
            # "https://sub.example.com",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
        ```
        
    
    ### 08 - Adicionando Djoser ao Django (PARA AUTH NO LUGAR DO TOKEN)
    
    - [x]  Digitar no terminal: `pip install djoser`
    - [x]  Adicionar em ************************************settings.py************************************ em installed apps `'djoser',`
    - [x]  Configurar no ************************************settings.py************************************ de acordo com abaixo
        - `Código:`
            
            ```python
            # Configurações do DJOSER para envio de email com links de ativações
            DJOSER = {
                'LOGIN_FIELD': 'email',
                'USER_CREATE_PASSWORD_RETYPE': False,
                'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
                'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
                'SEND_CONFIRMATION_EMAIL': True,
                'SET_USERNAME_RETYPE': True,
                'SET_PASSWORD_RETYPE': True,
                'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
                'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
                'ACTIVATION_URL': 'activate/{uid}/{token}',
                'SEND_ACTIVATION_EMAIL': True,
                'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
                'SERIALIZERS': {
                    'user_create': 'funetech.serializers.UserCreateSerializer',
                    'user': 'funetech.serializers.UserCreateSerializer',
                    'current_user': 'funetech.serializers.UserCreateSerializer',
                    'user_delete': 'djoser.serializers.UserDeleteSerializer',
                    'activation': 'djoser.serializers.ActivationSerializer', 
                },
                'EMAIL': {
                    'activation': 'djoser.email.ActivationEmail',
                    'confirmation': 'djoser.email.ConfirmationEmail',
                    'password_reset': 'djoser.email.PasswordResetEmail',
                },
                'PERMISSIONS':{
                'user_delete': ['rest_framework.permissions.IsAdminUser'] # not allow delete
                },
            }
            ```
            
    - [x]  Criar função ***UserActivationView*** em views, para ativar o usuário pelo link do email
        - `Código:`
            
            ```python
            from rest_framework.response import Response
            from rest_framework.views import APIView
            
            import requests
            
            # REALIZAR A ATIVAÇÃO DA CONTA APÓS CLICAR NO LINK DO DJOSER
            class UserActivationView(APIView):
                def get (self, request, uid, token):
                    protocol = 'https://' if request.is_secure() else 'http://'
                    web_url = protocol + request.get_host()
                    post_url = web_url + "/auth/users/activation/"
                    post_data = {'uid': uid, 'token': token}
                    result = requests.post(post_url, data = post_data)
                    content = result.text
                    return Response(content)
            ```
            
    - [x]  Configurar o arquivo ************************urls.py************************ para as urls do *Djoser*
        - `Código:`
            
            ```python
            from django.urls import include, path
            from rest_framework import routers
            from django.contrib import admin
            from funetech.views import UserActivationView
            
            from homenagem.views import HomenagemViewSet
            
            # importações para trabalhar com imagens
            from django.conf import settings
            from django.conf.urls.static import static
            
            router = routers.DefaultRouter()
            # SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
            router.register(r'homenagens', HomenagemViewSet, basename='Homenagem')
            
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include(router.urls)),
                path('auth/', include('djoser.urls')),
                # path('auth/', include('djoser.urls.jwt')),
                path('auth/', include('djoser.urls.authtoken')),
                # path('auth/', include('djoser.social.urls')),
                path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
            ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para caso vá trabalhar com imagens
            ```
            
    
    ## DEPLOY:
    
    ### RAILWAY
    
    - Instalar WHITENOISE para renderizar os STATIC FILES
    - Instalar PSYCOPG2 para utilizar banco de dados postgresql
    - Configurar Banco de Dados
    
    ### 09 - Realizando Deploy no Railway
    
    - [ ]  Digitar no cmd: `pip install whitenoise`
    - [ ]  Configurar o arquivo ************************settings.py************************ para funcionar o Whitenoise
        - `Código:`
            
            ```python
            # ADICIONAR EM INSTALLED APPS, ABAIXO DO DJANGO.CONTRIB.STATICFILES:
            'whitenoise.runserver_nostatic',
            
            # ADICIONAR EM MIDDLEWARE, ABAIXO DO SECURITY MIDDLEWARE:
            "whitenoise.middleware.WhiteNoiseMiddleware",
            
            # SUBSTITUIR O STATIC_URL PELO CÓDIGO ABAIXO:
            # WHITENOISE
            STATIC_URL = '/static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
            STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
            # WHITENOISE
            ```
            
    - [ ]  Digitar no cmd: `pip install psycopg2`
    - [ ]  Configurar o arquivo ************************settings.py************************ para funcionar o BD Postgresql
        - `Código:`
            
            ```python
            # SUBSTITUIR O DEFAULT SQLITE3 PELO ABAIXO 
            # (MUDAR AS VARIÁVEIS CONFORME O BD DO RAILWAY):
            
            'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'railway',
                    'USER': 'postgres',
                    'PASSWORD': 'VJO2TAL3wh2br8Tok0r4',
                    'HOST': 'containers-us-west-172.railway.app',
                    'PORT': '6254',
                }
            ```
            
    
    ## TODO:
    
    CONFIGURAR O AWS ELASTIC BEANSTALK PRA DEPLOY [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb)
    
    ## Links
    
    [The web framework for perfectionists with deadlines | Django (djangoproject.com)](https://www.djangoproject.com/)
    
    [Django · PyPI](https://pypi.org/project/Django/)
    
    [List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    
    [Entendendo o MTV do Django | Blog TreinaWeb](https://www.treinaweb.com.br/blog/entendendo-o-mtv-do-django)
    
    [O que é JSON? | Blog TreinaWeb](https://www.treinaweb.com.br/blog/o-que-e-json)
    
    [Home - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/)
    
    [O que é CORS e como resolver os principias erros | Blog TreinaWeb](https://www.treinaweb.com.br/blog/o-que-e-cors-e-como-resolver-os-principais-erros)
    
    [django-cors-headers · PyPI](https://pypi.org/project/django-cors-headers/)
    
    ## Problemas frequentes
    
    - Caso a virtualenv não esteja ativada no Windows, digite os seguintes comandos no terminal
        - Caso esteja utilizando o CMD:
            
            `.venv\Scripts\activate`
            
        - Caso esteja utilizando o PowerShell
            
            `.venv\Scripts\Activate.ps1`
            
    - Ao executar o comando `.venv\Scripts\Activate.ps1` no PoweShell exibe o erro de segurança como da imagem abaixo:
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33399956-48a4-46ae-8102-31a53a20ad75/Untitled.png)
        
        - Para resolver basta executar o comando `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, porém vale ressaltar que essa solução só funciona para o terminal ao qual o comando foi executado, caso abra um novo terminal o erro irá acontecer novamente e será necessário executar novamente o comando.
        - Para resolver de forma definitiva de forma que não seja necessário executar o comando toda vez que abrir o terminal é necessário fechar o terminal aberto no momento e então abrir um novo PoweShell com privilégios de administrador, para isso basta clicar com o botão direito no ícone do PowerShell e então selecionar a opção “Executar como administrador”
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3651981f-4645-425c-95e3-3b08e58120de/Untitled.png)
        
        - Com o novo PowerShell aberto execute o comando `Set-ExecutionPolicy Unrestricted` e logo em seguida digite a letra “A” para aceitar. Feito isso pode fechar esse PowerShell e então abrir um novo PowerShell normalmente que o comando de ativação da virtualenv não dará mais problema.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df3d25f1-5ebd-49bc-990d-f4b16c74f90e/Untitled.png)
        
        ## DJOSER:
        
        ### CASO DÊ ERRO AO ENVIAR A URL DO FRONTEND POR EMAIL:
        
        - SUBSTITUIR NO ARQUIVO ******************************************djoser/templates/password_reset****************************************** ONDE TIVER `{{ url }}` POR `{{ url|safe }}`
        
        [https://www.dicas-de-django.com.br/47-djoser](https://www.dicas-de-django.com.br/47-djoser)
        
        [https://saasitive.com/tutorial/token-based-authentication-django-rest-framework-djoser/](https://saasitive.com/tutorial/token-based-authentication-django-rest-framework-djoser/)