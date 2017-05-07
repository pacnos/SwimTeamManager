from django import template

register = template.Library()


@register.filter(name='b_text')
def bootstrap_text_input_filter(field):
    return field.as_widget(attrs={"class": "form-control"})
