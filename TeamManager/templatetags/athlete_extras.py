from django import template
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext as _

register = template.Library()


@register.filter(name="gender")
def male_female_filter(value):
    """
    Filter which handels the representation of the gender of an athlete
    :return: 
    """

    if value:
        return mark_safe("<i class=\"fa fa-male fa-fw\"></i> %s" % _("Male"))
    else:
        return mark_safe("<i class=\"fa fa-female fa-fw\"></i> %s" % _("Female"))


@register.filter(name="medical_table_color")
def medical_table_color(value):

    if value == 1:
        return mark_safe("background-color: #fcf8e3;")
    elif value == 2:
        return mark_safe("background-color: #f2dede;")
    else:
        return ""

