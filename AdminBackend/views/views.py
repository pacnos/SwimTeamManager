from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView


class UserManagementView(ListView):
    """
    View which shows the User management page
    """
    template_name = "admin/user_management.html"
    model = User
    context_object_name = "user_list"

    def get_context_data(self, **kwargs):
        context = super(UserManagementView, self).get_context_data(**kwargs)

        context["title"] = "User Management"

        return context


class DeleteAthleteView(DeleteView):
    """
    View which is used to delete an athlete
    """

    model = User
    success_url = reverse_lazy("Admin:overview")
