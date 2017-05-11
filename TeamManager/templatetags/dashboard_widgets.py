import datetime
from django import template

from TeamManager.models import Athlete

register = template.Library()


@register.inclusion_tag(filename="dashboard_widgets/last_medical_examination.html")
def last_medical_examination():
    """
    Shows an overview about the last medical examinations of the athletes
    :return: 
    """

    date_filter_warning = datetime.date.today() + datetime.timedelta(6 * 30)

    return {
        "overdue_medical": Athlete.objects.filter(last_medical__lte=datetime.date.today()),
        "upcoming_medical": Athlete.objects.filter(last_medical__lte=date_filter_warning)
    }
