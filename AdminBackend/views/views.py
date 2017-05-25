from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.base import TemplateView, View

from django.views.generic.edit import FormView

from AdminBackend.forms.forms import BasicUserForm, FullUserForm, MedicalMailForm
from AdminBackend.mixins.group_mixins import AdminPermissionRequiredMixin
from AdminBackend.models import MailSettings


class UserManagementView(AdminPermissionRequiredMixin, ListView):
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


class UserCreateView(AdminPermissionRequiredMixin, FormView):
    """
    View which is used to create a new user
    """
    context_object_name = "form"
    form_class = FullUserForm
    template_name = "admin/user_create.html"
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
        user.tmuser.group = group

        user.save()

        # Go to overview page
        return super(UserCreateView, self).form_valid(form)


class UserEditView(AdminPermissionRequiredMixin, FormView):
    """
    View which is used to edit a existing user
    """
    context_object_name = "form"
    form_class = BasicUserForm
    template_name = "admin/user_edit.html"
    success_url = reverse_lazy("AdminBackend:overview")

    def get_initial(self):
        """
        Returns the initial form data
        :return: 
        """

        user_object = User.objects.get(pk=self.kwargs["pk"])

        return {
            "username": user_object.username,
            "first_name": user_object.first_name,
            "last_name": user_object.last_name,
            "mail": user_object.email,
            "group": user_object.tmuser.get_group()
        }

    def get_context_data(self, **kwargs):
        context = super(UserEditView, self).get_context_data(**kwargs)

        context["title"] = "Edit User"
        context["fix_username"] = True

        return context

    def form_valid(self, form):
        """
        Called when the form was valid
        :param form: 
        :return: 
        """

        # Get the form data
        group = form.cleaned_data["group"]

        # Get the user
        user = User.objects.get(pk=self.kwargs["pk"])

        user.first_name = form.cleaned_data["first_name"]
        user.last_name = form.cleaned_data["last_name"]
        user.email = form.cleaned_data["mail"]

        # Handle the Rights
        user.tmuser.group = group

        user.save()

        # Go to overview page
        return super(UserEditView, self).form_valid(form)


class TMLoginView(LoginView):
    template_name = "admin/login.html"

    def get_context_data(self, **kwargs):
        context = super(TMLoginView, self).get_context_data(**kwargs)

        context["title"] = "Login"

        return context


class MailSettingsView(View):
    """
    View which shows the mail settings
    """
    form_class = MedicalMailForm
    template_name = "admin/mail_settings.html"
    data_object = {
        'title': "Mail Settings",
    }

    def get(self, request, *args, **kwargs):
        """
        Get method
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        self.data_object["medical_success"] = False

        # Try to get available medical data
        form = self.__get_medical_form()

        self.data_object["medical_form"] = form

        return render(request, self.template_name, self.data_object)

    def post(self, request, *args, **kwargs):
        """
        Post method
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        self.data_object["medical_success"] = False

        # Load standard forms
        form = self.__get_medical_form()

        # Determine action
        action = self.request.POST['action']

        # Medical Mail form selected
        if action=="medical_mail":
            form = self.form_class(request.POST, prefix="medical_mail")

            if form.is_valid():
                self.__update_medical_mail_settings(form.cleaned_data["medical_mail_title"],
                                                    form.cleaned_data["medical_mail_text"])
                self.data_object["medical_success"] = True

        # Add forms to view and return
        self.data_object["medical_form"] = form

        return render(request, self.template_name, self.data_object)

    def __get_medical_form(self):
        """
        Returns the medical form
        :return: 
        """
        try:
            settings_object = MailSettings.objects.get(pk=1)
            form = self.form_class(instance=settings_object, prefix="medical_mail")
        except ObjectDoesNotExist as ex:
            form = self.form_class(prefix="medical_mail")

        return form

    def __update_medical_mail_settings(self, title, text):
        """
        Updates the medical Mail settings
        :param title: 
        :param text: 
        :return: 
        """

        try:
            settings_object = MailSettings.objects.get(pk=1)
        except ObjectDoesNotExist as ex:
            settings_object = MailSettings()

        settings_object.medical_mail_title = title
        settings_object.medical_mail_text = text

        settings_object.save()