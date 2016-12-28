from django.db import models


class Athlete(models.Model):
    """
    Class for the athletes
    """
    # Person Data
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_data = models.DateField()
    male = models.BooleanField()

    # Competition Data
    competitor_number = models.CharField(max_length=30)
    last_medical = models.DateField()

    # Address data
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    street = models.CharField(max_length=80)

    # Contact Data
    phone = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    mobile_phone_father = models.CharField(max_length=30)
    mail_father = models.EmailField()

    mobile_phone_mother = models.CharField(max_length=30)
    mail_mother = models.EmailField()