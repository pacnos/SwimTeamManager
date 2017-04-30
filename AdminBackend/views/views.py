from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormView

from AdminBackend.forms.forms import UserForm
from AdminBackend.utils import AVAILABLE_GROUPS


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


class UserCreateView(FormView):
    """
    View which is used to create a new user
    """
    context_object_name = "form"
    form_class = UserForm
    template_name = "admin/user_create_edit.html"
    success_url = reverse_lazy("AdminBackend:overview")

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)

        context["title"] = "Create User"

        return context

    def form_valid(self, form):
        """
        Called when the form was valid
        :param form: 
        :return: 
        """

        # Get the form data
        user_name = form.cleaned_data["username"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        mail = form.cleaned_data["mail"]
        password = form.cleaned_data["password"]
        group = form.cleaned_data["group"]

        # Create the user
        user = User.objects.create_user(user_name, mail, password)

        user.first_name = first_name
        user.last_name = last_name

        # Handle the Rights
        user.groups.clear()
        if group == "AT" or group == "CO":
            group = Group.objects.get(name=AVAILABLE_GROUPS[group])
            user.groups.add(group)
        else:
            user.is_superuser = True

        user.save()

        # Go to overview page
        return super(UserCreateView, self).form_valid(form)
