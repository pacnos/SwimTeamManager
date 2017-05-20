from django.forms.fields import DateField, IntegerField, CharField
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

    birth_date = DateField(input_formats=["%d.%m.%Y"])
    last_medical = DateField(input_formats=["%d.%m.%Y"], required=False)


class MedicalUpdateForm(Form):
    """
    Form which handles the medical update
    """

    user_id = CharField()
    last_medical = DateField(input_formats=["%d.%m.%Y"])
