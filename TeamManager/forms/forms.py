from django.forms.fields import DateField, IntegerField, CharField, FileField
from django.forms.forms import Form
from django.forms.models import ModelForm

from TeamManager.models import Athlete


class AthleteForm(ModelForm):
    """
    Class which represents the athlete model form
    """
    class Meta:
        model = Athlete
        fields = "__all__"

    birth_date = DateField(localize=True)
    last_medical = DateField(localize=True, required=False)


class MedicalUpdateForm(Form):
    """
    Form which handles the medical update
    """

    user_id = CharField()
    last_medical = DateField(localize=True)


class AthleteCSVImportForm(Form):
    """
    Form which handles the athlete csv import
    """

    file = FileField(allow_empty_file=False)

