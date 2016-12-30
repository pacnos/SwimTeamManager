from django.conf.urls import url

from . import views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^athlete_management/$', views.AthleteManagementView.as_view(), name='athleteManagement'),
    url(r'^athlete_management/athlete/$', views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
    url(r'^athlete_management/athlete/([0-9]+)/$', views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
]
