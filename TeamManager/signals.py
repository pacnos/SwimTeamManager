from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from TeamManager.models import Athlete, MedicalWarnState


@receiver(pre_save, sender=Athlete)
def reset_medical_warn_state(sender, instance, raw, using, update_fields, **kwargs):
    """
    Check if the medical date was changed, then reset warning too
    :param instance: 
    :param created: 
    :param raw: 
    :param using: 
    :param update_fields: 
    :return: 
    """

    try:
        if Athlete.objects.get(pk=instance.pk).last_medical != instance.last_medical:
            if hasattr(instance, 'medical_warn_state'):
                medical_warn_state = instance.medical_warn_state
                medical_warn_state.three_months_warning=False
                medical_warn_state.week_warning=False
            else:
                instance.medical_warn_state = MedicalWarnState(three_months_warning=False, week_warning=False, athlete=instance)

    except ObjectDoesNotExist as ex:
        pass


@receiver(post_save, sender=Athlete)
def athlete_created(sender, instance, created, raw, using, update_fields, **kwargs):
    """
    Called after the save of the Athlete model
    :param sender: 
    :param instance: 
    :param raw: 
    :param using: 
    :param update_fields: 
    :param kwargs: 
    :return: 
    """

    if created:
        medical_warn_state = MedicalWarnState(three_months_warning=False, week_warning=False, athlete=instance)
        medical_warn_state.save()
    else:
        instance.medical_warn_state.save()