from django.conf.urls import url

from . import views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^athlete_management/$', views.AthleteManagementView.as_view(), name='athleteManagement'),
]
