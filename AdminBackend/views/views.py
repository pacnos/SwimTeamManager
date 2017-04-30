from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """
    View which shows the login dashboard
    """
    template_name = "base_backend.html"