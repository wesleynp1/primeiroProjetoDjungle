#para criar um projeto
django-admin startproject MeuSiteDjango .

#para rodar o servidor
python manage.py runserver

#ao alterar o model, use este comando para aplicar as alterações no database.
#OBS: talvez seja necessario excluir a pasta 'migrations',
#principalmente se mexeu numa chave estrangeira para não dar erro de compatibilidade
python manage.py makemigrations <model>

#Para de fato aplicar as migrações criadas no comando anterior para o banco de dados use:
python manage.py migrate

#Mostra o sql que gerou a migração no banco de dados
python manage.py sqlmigrate produtos 0001

#Para interagir com os objetos entre outras coisas
python manage.py shell

#Para criar a conta de admin
python manage.py createsuperuser