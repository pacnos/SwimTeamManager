from django.forms.fields import DateField
from django.forms.models import ModelForm
from django.forms import DateInput

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
