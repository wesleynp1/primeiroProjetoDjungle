#para criar um projeto
django-admin startproject MeuSiteDjango .

python manage.py startapp <app>

#para rodar o servidor
python manage.py runserver

#ao alterar o model, use este comando para aplicar as alterações no database.
#OBS: talvez seja necessario excluir a pasta 'migrations',
#principalmente se mexeu numa chave estrangeira para não dar erro de compatibilidade
python manage.py makemigrations <app>

#Para de fato aplicar as migrações criadas no comando anterior para o banco de dados use:
python manage.py migrate

#Mostra o sql que gerou a migração no banco de dados
python manage.py sqlmigrate produtos 0001

#Para interagir com os objetos entre outras coisas
python manage.py shell

#Para criar a conta de admin
python manage.py createsuperuser

#para realizar testes no shell use
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> cliente = Client()
#divirta-se :)

#para migrar para o postgreSQL é necessário o seguinte pacote:
pip install psycopg2-binary

#para usar arquivo .env instale
pip install python-dotenv

#quando realizar testes e receber um acess denied use
ALTER USER your_django_user CREATEDB;