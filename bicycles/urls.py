from bicycles import views
from django.urls import path

urlpatterns = [
    # path('bicycles/', views.main),
    path('bicycles/<int:id>/', views.detail_bicycles, name='detail_bicycles'),
    path('', views.main, name='main'),
    path('cataloque/', views.catalogue, name='catalogue'),
    path('equipments/', views.equipments, name='equipments'),
]