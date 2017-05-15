import datetime
from django.db import models


class Athlete(models.Model):
    """
    Class for the athletes
    """
    date_filter_warning = datetime.date.today() + datetime.timedelta(6 * 30)
    date_filter_overdue = datetime.date.today()

    # Person Data
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    male = models.BooleanField()

    # Competition Data
    competitor_number = models.CharField(max_length=30, null=True, blank=True)
    last_medical = models.DateField(null=True, blank=True)

    # Address data
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    street = models.CharField(max_length=80)

    # Contact Data
    phone = models.CharField(max_length=30, null=True, blank=True)
    mobile_phone = models.CharField(max_length=30, null=True, blank=True)
    mail = models.CharField(max_length=30, null=True, blank=True)

    mobile_phone_father = models.CharField(max_length=30, null=True, blank=True)
    mail_father = models.EmailField(null=True, blank=True)

    mobile_phone_mother = models.CharField(max_length=30, null=True, blank=True)
    mail_mother = models.EmailField(null=True, blank=True)

    @property
    def medical_warn_state(self):
        """
        Returns the Medical warn state:
        2: Overdue
        1: Warning
        0: OK
        :return: 
        """

        if self.last_medical <= self.date_filter_overdue:
            return 2
        elif self.last_medical <= self.date_filter_warning:
            return 1
        else:
            return 0
