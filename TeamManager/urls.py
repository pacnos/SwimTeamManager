from django.conf.urls import url

from . import views, json_views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^athlete_management/$', views.AthleteManagementView.as_view(), name='athleteManagement'),
    url(r'^athlete_management/athlete/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
    url(r'^athlete_management/athlete/([0-9]+)/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
]
