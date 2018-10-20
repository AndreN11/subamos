from django.conf.urls import url
from aplicacion import views
urlpatterns = [
    url(r'^usuarios/$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),

    url(r'^categoria/$', views.CategoriaList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view()),
]