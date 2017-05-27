from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class TMUser(models.Model):
    """
    Class which represents a team manager user
    """
    GROUP_ATHLETE = "AT"
    GROUP_COACH = "CO"
    GROUP_ADMIN = "AD"

    GROUP_CHOICES = (
        (GROUP_ATHLETE, _("Athlete")),
        (GROUP_COACH, _("Coach")),
        (GROUP_ADMIN, _("Admin"))
    )

    GROUP_TRANSLATIONS = {
        GROUP_ATHLETE: _("Athlete"),
        GROUP_COACH: _("Coach"),
        GROUP_ADMIN: _("Admin")
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=2, choices=GROUP_CHOICES, default=GROUP_ATHLETE)

    def get_group(self):
        """
        Returns the group of the user
        :return: 
        """

        if self.user.is_superuser:
            return self.GROUP_ADMIN
        else:
            return self.group

    def get_group_translation(self):
        """
        Returns the translation of a group
        :return: 
        """

        return self.GROUP_TRANSLATIONS[self.get_group()]

    def is_coach_or_admin(self):
        """
        Checks if the given user is coach or admin
        :return: 
        """
        group = self.get_group()
        return group != self.GROUP_ATHLETE

    def is_admin(self):
        """
        Checks if the given user is admin
        :return: 
        """

        return self.get_group() == self.GROUP_ADMIN

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            TMUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.tmuser.save()


class MailSettings(models.Model):
    """
    Model which contains the Mail settings
    """

    medical_mail_title = models.CharField(max_length=150)
    medical_mail_text = models.TextField()
    medical_mail_cc = models.EmailField()


class GeneralSettings(models.Model):
    """
    Class which holds the general settings
    """

    NO_SECURITY = "NO"
    TLS = "TLS"
    SSL = "SSL"

    GROUP_CHOICES = (
        (NO_SECURITY, _("None")),
        (TLS, "TLS"),
        (SSL, "SSL")
    )

    # Mail Settings
    email_host = models.CharField('EMAIL_HOST', max_length=1024)
    email_port = models.PositiveSmallIntegerField('EMAIL_PORT', default=587)
    email_host_user = models.CharField('EMAIL_HOST_USER', max_length=255)
    email_host_password = models.CharField('EMAIL_HOST_PASSWORD', max_length=255)

    email_security = models.CharField(max_length=3, choices=GROUP_CHOICES, default=NO_SECURITY)

    email_sender_name = models.CharField('EMAIL_SENDER', max_length=200)
    email_sender_mail = models.EmailField('EMAIL_SENDER')



