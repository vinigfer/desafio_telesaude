from django.conf.urls import url

from desafio import views

urlpatterns = [
    url(r'^solicitante$', views.solicitante_list, name='solicitante_list'),
    url(r'^solicitante_new$', views.solicitante_create, name='solicitante_new'),
    url(r'^solicitante_edit/(?P<pk>\d+)$', views.solicitante_update, name='solicitante_edit'),
    url(r'^solicitante_delete/(?P<pk>\d+)$', views.solicitante_delete, name='solicitante_delete'),
    ###
    url(r'^teleconsultor$', views.teleconsultor_list, name='teleconsultor_list'),
    url(r'^teleconsultor_new$', views.teleconsultor_create, name='teleconsultor_new'),
    url(r'^teleconsultor_edit/(?P<pk>\d+)$', views.teleconsultor_update, name='teleconsultor_edit'),
    url(r'^teleconsultor_delete/(?P<pk>\d+)$', views.teleconsultor_delete, name='teleconsultor_delete'),
    ###
    url(r'^solicitacao', views.solicitacao_list, name='solicitacao_list'),
    url(r'^solicitacao_new$', views.solicitacao_create, name='solicitacao_new'),
    url(r'^solicitacao_edit/(?P<pk>\d+)$', views.solicitacao_update, name='solicitacao_edit'),
    url(r'^solicitacao_delete/(?P<pk>\d+)$', views.solicitacao_delete, name='solicitacao_delete'),
]