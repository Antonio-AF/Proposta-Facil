from django.urls import path

from .views import modelo, painel, dologin, store, signup, proposta, dashboard, login_form, cadastro

urlpatterns = [
    path('', modelo, name='login_form'),
    path('painel/', painel, name='painel'),
    path('dologin/', dologin),
    path('store/', store, name='store'),
    path('proposta/', proposta, name='proposta'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login_form/', login_form, name='login_form'),
    path('cadastro/', cadastro, name='cadastro'),
]

