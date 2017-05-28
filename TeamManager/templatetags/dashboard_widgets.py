import datetime
from django import template
from django.conf import settings
from django.db.models import Q

from TeamManager.models import Athlete

register = template.Library()


@register.inclusion_tag(filename="dashboard_widgets/last_medical_examination.html")
def last_medical_examination():
    """
    Shows an overview about the last medical examinations of the athletes
    :return: 
    """

    date_filter_warning = datetime.date.today() + datetime.timedelta(settings.MEDICAL_WARN_TIME)
    today = datetime.date.today()

    return {
        "overdue_medical": Athlete.objects.filter(Q(last_medical__lte=today) | Q(last_medical__isnull=True)).order_by("last_medical"),
        "upcoming_medical": Athlete.objects.filter(last_medical__lte=date_filter_warning, last_medical__gt=today).order_by("last_medical")
    }
