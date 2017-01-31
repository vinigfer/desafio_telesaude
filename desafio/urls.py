from django.conf.urls import patterns, url

from desafio import views

urlpatterns = [
    url(r'^solicitante$', views.solicitante_list, name='solicitante_list'),
    url(r'^solicitante_new$', views.solicitante_create, name='solicitante_new'),
    url(r'^solicitante_edit/(?P<pk>\d+)$', views.solicitante_update, name='solicitante_edit'),
    url(r'^solicitante_delete/(?P<pk>\d+)$', views.solicitante_delete, name='solicitante_delete'),
]