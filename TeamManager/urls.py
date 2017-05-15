from django.conf.urls import url

from TeamManager.views import json_views, views

app_name = 'TeamManager'

urlpatterns = [
    url(r'^$', views.AthleteManagementView.as_view(), name='athleteManagement'),

    url(r'^athlete/create/$', views.CreateAthleteView.as_view(), name='athleteCreate'),
    url(r'^athlete/edit/(?P<pk>[0-9]+)/$', views.EditAthleteView.as_view(), name='athleteEdit'),


    url(r'^athlete/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),
    url(r'^athlete/([0-9]+)/$', json_views.AthleteContactDetailsJSON.as_view(), name='athleteContact'),

    url(r'^athlete/delete/$', json_views.AthleteDeleteJSON.as_view(), name='athleteDelete'),
    url(r'^athlete/delete/([0-9]+)/$', json_views.AthleteDeleteJSON.as_view(), name='athleteDelete'),

    # Athlete sub views
    url(r'^athlete/medical/$', views.MedicalView.as_view(), name='athleteMedical'),
]
