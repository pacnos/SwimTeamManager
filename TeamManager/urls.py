from django.conf.urls import url

from TeamManager.views import json_views, views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^athlete_management/$', views.AthleteManagementView.as_view(), name='athleteManagement'),

    url(r'^athlete_management/athlete/create/$', views.CreateAthleteView.as_view(), name='athleteCreate'),
    url(r'^athlete_management/athlete/edit/(?P<pk>[0-9]+)/$', views.EditAthleteView.as_view(), name='athleteEdit'),


    url(r'^athlete_management/athlete/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
    url(r'^athlete_management/athlete/([0-9]+)/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),

url(r'^athlete_management/athlete/delete/$', json_views.AthleteDeleteJSON.as_view(), name='athleteDelete'),
    url(r'^athlete_management/athlete/delete/([0-9]+)/$', json_views.AthleteDeleteJSON.as_view(), name='athleteDelete')
]
