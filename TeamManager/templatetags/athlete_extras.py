from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name="gender")
def male_female_filter(value):
    """
    Filter which handels the representation of the gender of an athlete
    :return: 
    """

    if value:
        return mark_safe("<i class=\"fa fa-male\"></i> Male")
    else:
        return mark_safe("<i class=\"fa fa-female\"></i> Female")


@register.filter(name="medical_table_color")
def medical_table_color(value):

    if value == 1:
        return mark_safe("background-color: #fcf8e3;")
    elif value == 2:
        return mark_safe("background-color: #f2dede;")
    else:
        return ""

