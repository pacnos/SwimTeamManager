from django.conf.urls import url

from AdminBackend.views import views, json_views

app_name = 'AdminBackend'

urlpatterns = [
    url(r'^$', views.UserManagementView.as_view(), name='overview'),

    url(r'^user/create/$', views.UserCreateView.as_view(), name='userCreate'),
    url(r'^user/edit/(?P<pk>[0-9]+)/$', views.UserEditView.as_view(), name='userEdit'),

    url(r'^user/delete/$', json_views.UserDeleteJSON.as_view(), name='userDelete'),
    url(r'^user/delete/([0-9]+)/$', json_views.UserDeleteJSON.as_view(), name='userDelete')
]
