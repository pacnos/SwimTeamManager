from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    """
    View which shows the login dashboard
    """
    template_name ="base_backend.html"