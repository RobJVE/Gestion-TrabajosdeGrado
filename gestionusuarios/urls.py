from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('logout', views.logout),
    path('tipo', views.tipo_view, name='tipo_usuario'),
    path('nuevo', views.usuario_view, name='crear_usuario'),
    path('term', views.term_view, name='term_nuevo'),
    path('consultaterm', views.consultar_term, name='term_consulta'),
    path('consultatipopersona', views.consultar_tipopersona, name='tipo_consulta'),
    path('nuevapropuesta', views.propuesta_view, name='crear_propuesta'),
    path('consultarpersona', views.consultar_persona, name='consultar_persona'),
    path('consultarcedula', views.consultar_cedula, name='consultar_cedula'),
    path('consultarpropuesta', views.consultar_propuesta, name='consultar_propuesta'),
    path('<int:idpersona>/editarpersona', views.editar_persona, name='editar_persona'),
    path('<int:periodo>/editarterm', views.editar_term, name='editar_term'),
    path('<int:id>/editartipo', views.editar_tipopersona, name='editar_tipo'),
]