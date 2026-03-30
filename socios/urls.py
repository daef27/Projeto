from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('esportes/', views.esportes_view, name='esportes'),
    path('parceiros/', views.parceiros_view, name='parceiros'),

]