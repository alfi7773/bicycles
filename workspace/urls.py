from django.urls import path

from workspace import views

urlpatterns = [
    path('create-bicycles/', views.create_bicycles, name='create_bicycles'),
    path('update-bicycles/<int:id>', views.update_bicycles, name='update_bicycles'),
    path('delete-bicycles/<int:id>', views.delete_bicycle, name='delete_bicycle'),
    path('', views.workspace, name='workspace'),
]