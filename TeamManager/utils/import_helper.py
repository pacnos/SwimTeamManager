import csv
import datetime
from django.conf import settings

from TeamManager.models import Athlete


def import_athlete_csv(file):
    """
    Handles the import of a athlete csv file
    :param file:
    :return:
    """
    # Get the reader
    csv_reader = csv.reader(file, delimiter=';', quotechar='"')

    # Iterate through the data
    line_count = 0
    for row in csv_reader:

        # Ignore title line
        if line_count == 0:
            line_count += 1
            continue

        # Create the athlete objects
        athlete = Athlete()
        # Basic data
        athlete.first_name = row[0].strip()
        athlete.last_name = row[1].strip()
        athlete.birth_date = __parse_date(row[2])
        athlete.male = __parse_gender(row[3])

        # Competition details
        athlete.last_medical = __parse_date(row[4])
        athlete.competitor_number = row[5].strip()

        # Address
        athlete.street = row[6].strip()
        athlete.zip_code = row[7].strip()
        athlete.city = row[8].strip()

        # Contact athlete
        athlete.phone = row[9].strip()
        athlete.mobile_phone = row[10].strip()
        athlete.mail = row[11].strip()

        # Contact mother
        athlete.mobile_phone_mother = row[12].strip()
        athlete.mail_mother = row[13].strip()

        # Contact father
        athlete.mobile_phone_father = row[14].strip()
        athlete.mail_father = row[15].strip()

        # Save the athlete
        athlete.save()




def __parse_date(date_string):
    """
    Function to parse the birth date
    :param date_string:
    :return:
    """
    date_string = date_string.strip()

    if date_string == "":
        return None

    datetime_obj = datetime.datetime.strptime(date_string, settings.IMPORT_DATE_FORMAT)

    return datetime_obj.date()


def __parse_gender(gender_string):
    """
    Function to parse the gender of an athlete
    :param gender_string:
    :return:
    """
    gender_string = gender_string.strip()

    if gender_string == "True" or gender_string == "1" or gender_string.lower() == "male" or gender_string.lower() == "m":
        return True
    else:
        return False