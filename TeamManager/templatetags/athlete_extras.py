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
