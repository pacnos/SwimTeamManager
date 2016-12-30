import json
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views import View

from TeamManager.models import Athlete


class AthleteContactDetailsJSON(View):
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
        json_athlete = json.dumps(model_to_dict(athlete_object))

        return HttpResponse(json_athlete, content_type="application/json")