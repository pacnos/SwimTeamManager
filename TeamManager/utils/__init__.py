from django.conf import settings
from django.utils import formats


def get_current_short_date_format():
    """
    Returns the current short date format
    :return: 
    """
    return formats.get_format("SHORT_DATE_FORMAT", lang=settings.LANGUAGE_CODE)


def get_datepicker_date_format():
    """
    Returns a date format which can work as an input description for the bootstrap date picker component 
    :return: 
    """

    date_format = get_current_short_date_format()

    # Handle day
    date_format = date_format.replace("d", "dd")

    # Handle month
    date_format = date_format.replace("m", "mm")

    # Handle year
    date_format = date_format.replace("y", "yy")
    date_format = date_format.replace("Y", "yyyy")

    return date_format
