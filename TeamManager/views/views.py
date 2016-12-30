from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from TeamManager.models import Athlete


class DashboardView(TemplateView):
    """
    View which shows the login dashboard
    """
    template_name = "base_backend.html"


class AthleteManagementView(ListView):
    """
    View which shows the data of some athletes
    """
    template_name = "team_manager/athlete_management.html"
    model = Athlete
    context_object_name = "athlete_list"

    def get_context_data(self, **kwargs):
        context = super(AthleteManagementView, self).get_context_data(**kwargs)

        context["title"] = "Athlete Management"

        return context








