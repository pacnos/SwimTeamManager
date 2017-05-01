from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TMUser(models.Model):
    """
    Class which represents a team manager user
    """
    GROUP_ATHLETE = "AT"
    GROUP_COACH = "CO"
    GROUP_ADMIN = "AD"

    GROUP_CHOICES = (
        (GROUP_ATHLETE, "Athlete"),
        (GROUP_COACH, "Coach"),
        (GROUP_ADMIN, "Admin")
    )

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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            TMUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.tmuser.save()
