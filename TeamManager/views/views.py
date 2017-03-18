from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from TeamManager.forms.forms import AthleteForm
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


class CreateAthleteView(CreateView):
    """
    View which is used to create a new athlete
    """
    model = Athlete
    context_object_name = "form"
    form_class = AthleteForm
    template_name = "team_manager/athlete_create_edit.html"
    success_url = reverse_lazy("TeamManager:athleteManagement")

    def get_context_data(self, **kwargs):
        context = super(CreateAthleteView, self).get_context_data(**kwargs)

        context["title"] = "Create Athlete"

        return context


class EditAthleteView(UpdateView):
    """
    View which is used to edit an athlete
    """
    model = Athlete
    context_object_name = "form"
    form_class = AthleteForm
    template_name = "team_manager/athlete_create_edit.html"
    success_url = reverse_lazy("TeamManager:athleteManagement")

    def get_context_data(self, **kwargs):
        context = super(EditAthleteView, self).get_context_data(**kwargs)

        context["title"] = "Edit Athlete"

        return context


class DeleteAthleteView(DeleteView):
    """
    View which is used to delete an athlete
    """

    model = Athlete
    success_url = reverse_lazy("TeamManager:athleteManagement")















