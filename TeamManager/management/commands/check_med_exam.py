import datetime

import logging

from dateutil.relativedelta import relativedelta

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from django.core.management import BaseCommand

from AdminBackend.models import MailSettings, GeneralSettings
from TeamManager.models import Athlete

from django.conf import settings


class Command(BaseCommand):
    """
    Command class, checks the medical examination validation
    """
    help = 'Sends the warn mails about missing medical examinations'

    logger = logging.getLogger(__name__)
    _from = None

    def handle(self, *args, **options):
        """
        Called when the command was executed
        :param args: 
        :param options: 
        :return: 
        """
        # Load the settings
        try:
            mail_settings = MailSettings.objects.get(pk=1)
            general_settings = GeneralSettings.objects.get(pk=1)
        except ObjectDoesNotExist as ex:
            self.logger.error("Can't load configuration data")

        # Build the from part
        self._from = "%s <%s>" % (general_settings.email_sender_name, general_settings.email_sender_mail)

        # Get the mail backend
        use_ssl = False
        use_tls = False
        if general_settings.email_security == GeneralSettings.SSL:
            use_ssl = True
        elif general_settings.email_security == GeneralSettings.TLS:
            use_tls = True

        if settings.DEBUG:
            mail_backend = ConsoleEmailBackend()
        else:
            mail_backend = EmailBackend(host=general_settings.email_host, port=general_settings.email_port,
                                        username=general_settings.email_host_user,
                                        password=general_settings.email_host_password, use_ssl=use_ssl, use_tls=use_tls)

        # Handle the warning athletes
        #############################
        date_filter_warning = datetime.date.today() + datetime.timedelta(settings.MEDICAL_WARN_TIME) + \
            relativedelta(years=-1)

        athlete_list = Athlete.objects.filter(last_medical__lte=date_filter_warning,
                                              medical_warn_state__first_warning=False)

        for athlete in athlete_list:
            self.send_mail(athlete, mail_settings, mail_backend)
            athlete.medical_warn_state.first_warning = True
            athlete.save()

        # Handle the second warning
        #############################
        date_filter_second_warning = datetime.date.today() + datetime.timedelta(settings.SECOND_MEDICAL_WARN_TIME) \
            + relativedelta(years=-1)

        athlete_list = Athlete.objects.filter(last_medical__lte=date_filter_second_warning,
                                              medical_warn_state__second_warning=False)

        for athlete in athlete_list:
            self.send_mail(athlete, mail_settings, mail_backend)
            athlete.medical_warn_state.second_warning = True
            athlete.save()

    def send_mail(self, athlete, mail_settings, mail_backend):
        """
        Function which sends the medical mail
        :param mail_backend: 
        :param mail_settings: 
        :param athlete: 
        :return: 
        """

        # Create the body
        base_body = mail_settings.medical_mail_text
        base_body = base_body.replace("__FIRST_NAME__", athlete.first_name).replace("__LAST_NAME__", athlete.last_name) \
            .replace("__MEDICAL_END_DATE__", athlete.last_medical.strftime("%d.%m.%Y"))

        # Create the to list
        mail_to_list = []
        if athlete.mail is not None:
            mail_to_list.append(athlete.mail)

        if athlete.mail_father is not None:
            mail_to_list.append(athlete.mail_father)

        if athlete.mail_mother is not None:
            mail_to_list.append(athlete.mail_mother)

        if len(mail_to_list) == 0:
            self.logger.error("Didn't find any valid mail address for athlete %s %s" % (athlete.first_name,
                                                                                        athlete.last_name))
            return

        # Build the E-Mail
        email = EmailMessage(
            subject=mail_settings.medical_mail_title,
            body=base_body,
            from_email=self._from,
            to=mail_to_list,
            cc=[mail_settings.medical_mail_cc],
            connection=mail_backend
        )

        email.send()
