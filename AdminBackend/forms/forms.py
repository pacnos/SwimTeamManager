from django import forms

from AdminBackend.models import TMUser, MailSettings


class BasicUserForm(forms.Form):
    """
    Class which represents a form for a given user
    """

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.EmailField()

    group = forms.ChoiceField(choices=TMUser.GROUP_CHOICES)


class FullUserForm(BasicUserForm):
    """
    UserForm including password
    """
    password = forms.CharField()


class PasswordResetForm(forms.Form):
    """
    Form to reset a user password
    """

    password = forms.CharField()
    userId = forms.CharField()


class MedicalMailForm(forms.ModelForm):
    """
    Form which handles the input for the medical user data
    """
    class Meta:
        model = MailSettings
        fields = ['medical_mail_title', 'medical_mail_text']


