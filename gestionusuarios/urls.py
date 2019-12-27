from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('logout', views.logout),
    path('nuevo', views.usuario_view, name='crear_usuario'),
    path('nuevapropuesta', views.propuesta_view, name='crear_propuesta')
]