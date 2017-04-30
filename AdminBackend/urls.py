from django.conf.urls import url

from AdminBackend import views

app_name = 'Admin'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='overview'),
]
