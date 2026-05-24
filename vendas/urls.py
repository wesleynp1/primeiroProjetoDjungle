from django.urls import path
from . import views

app_name = 'vendas'
urlpatterns = [
    path('', views.index, name="index"),
    path('form/add', views.add_form, name="add_form"),
    path('add', views.add, name="add"),
    path('form/delete/<int:id>', views.delete_form, name="delete_form"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('form/edit/<int:id>', views.edit_form, name="edit_form"),
    path('edit/<int:id>', views.edit, name="edit"),
]