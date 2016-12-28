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
