import json

from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views import View

from AdminBackend.mixins.group_mixins import CoachPermissionRequiredMixin
from TeamManager.models import Athlete
from TeamManager.utils import json_helper


class AthleteContactDetailsJSON(CoachPermissionRequiredMixin, View):
    """
    Returns Details to a specific athlete
    """

    def get(self, request, args=None):
        """
        Get Method
        :param request:
        :return:
        """

        if args is None:
            return HttpResponseBadRequest()

        # Load object from database
        athlete_object = Athlete.objects.get(pk=self.args[0])
        data_dict = model_to_dict(athlete_object)
        json_athlete = json.dumps(data_dict, default=json_helper.json_serial)

        return HttpResponse(json_athlete, content_type="application/json")


class AthleteDeleteJSON(CoachPermissionRequiredMixin, View):
    """
    Deletes an Athlete
    """

    def get(self, request, args=None):
        """
        Get Method
        :param request:
        :param args:
        :return:
        """

        if args is None:
            return HttpResponseBadRequest()

        try:
            athlete = Athlete.objects.get(pk=self.args[0])
            athlete.delete()
        except ObjectDoesNotExist as ex:
            return HttpResponseBadRequest("Can't find athlete to delete")

        return HttpResponse()