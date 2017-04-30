from django import forms

from AdminBackend.utils import AVAILABLE_RIGHT_GROUPS


class UserForm(forms.Form):
    """
    Class which represents a form for a given user
    """

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.EmailField()
    password = forms.CharField()

    group = forms.ChoiceField(choices=AVAILABLE_RIGHT_GROUPS)
