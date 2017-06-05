from django.urls.base import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from AdminBackend.mixins.group_mixins import CoachPermissionRequiredMixin, AthletePermissionRequiredMixin
from TeamManager.forms.forms import AthleteForm, AthleteCSVImportForm
from TeamManager.models import Athlete
from TeamManager.utils import get_datepicker_date_format


class DashboardView(AthletePermissionRequiredMixin, TemplateView):
    """
    View which shows the login dashboard
    """
    template_name = "team_manager/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        context["title"] = _("Dashboard")

        return context


class AthleteManagementView(CoachPermissionRequiredMixin, ListView):
    """
    View which shows the data of some athletes
    """
    template_name = "team_manager/athlete_management.html"
    model = Athlete
    context_object_name = "athlete_list"
    ordering = "-birth_date"


    def get_context_data(self, **kwargs):
        context = super(AthleteManagementView, self).get_context_data(**kwargs)

        context["title"] = _("Athlete Management")
        context["form"] = AthleteCSVImportForm()

        return context


class CreateAthleteView(CoachPermissionRequiredMixin, CreateView):
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

        context["title"] = _("Create Athlete")
        context["datepicker_format"] = get_datepicker_date_format()

        return context


class EditAthleteView(CoachPermissionRequiredMixin, UpdateView):
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

        context["title"] = _("Edit Athlete")
        context["datepicker_format"] = get_datepicker_date_format()

        return context


class MedicalView(CoachPermissionRequiredMixin, ListView):
    """
    View which shows an overview about the medical examiniations of the athlete
    """

    context_object_name = "athlete_list"
    model = Athlete
    ordering = "last_medical"
    template_name = "team_manager/medical_view.html"

    def get_context_data(self, **kwargs):
        context = super(MedicalView, self).get_context_data(**kwargs)

        context["title"] = _("Medical Examination Overview")
        context["datepicker_format"] = get_datepicker_date_format()

        return context
