from django import forms

from AdminBackend.utils import AVAILABLE_RIGHT_GROUPS


class BasicUserForm(forms.Form):
    """
    Class which represents a form for a given user
    """

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.EmailField()

    group = forms.ChoiceField(choices=AVAILABLE_RIGHT_GROUPS)


class FullUserForm(BasicUserForm):
    """
    UserForm including password
    """
    password = forms.CharField()
