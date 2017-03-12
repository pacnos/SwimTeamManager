import json
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views import View

from TeamManager.models import Athlete
from TeamManager.utils import json_helper


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
        dict = model_to_dict(athlete_object)
        json_athlete = json.dumps(dict, default=json_helper.json_serial)

        return HttpResponse(json_athlete, content_type="application/json")