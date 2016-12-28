from django.conf.urls import url

from . import views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
]
