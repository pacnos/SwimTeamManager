import json
from io import TextIOWrapper

from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views import View

from AdminBackend.mixins.group_mixins import CoachPermissionRequiredMixin
from TeamManager.forms.forms import MedicalUpdateForm, AthleteCSVImportForm
from TeamManager.models import Athlete
from TeamManager.utils import json_helper
from TeamManager.utils.import_helper import import_athlete_csv


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
            return HttpResponseBadRequest(_("Can't find athlete to delete"))

        return HttpResponse()


class AthleteMedicalOverviewUpdate(CoachPermissionRequiredMixin, View):
    """
    Returns the athlete medical data
    """

    def post(self, request, *args, **kwargs):
        """
        Post Method
        :param request:
        :param args:
        :return:
        """

        form = MedicalUpdateForm(request.POST)

        if form.is_valid():
            medical_date = form.cleaned_data["last_medical"]
            user_id = form.cleaned_data["user_id"]

            # Update the athlete object
            athlete = Athlete.objects.get(pk=user_id)
            athlete.last_medical = medical_date
            athlete.save()

            # Create the response
            athlete_list = Athlete.objects.all().order_by("last_medical")

            return render(request, "team_manager/ajax_parts/medical_table_body.html", {'athlete_list': athlete_list})
        else:
            return HttpResponseBadRequest(_("The given data are not valid"))


class UploadAthleteImportCSVJSON(CoachPermissionRequiredMixin, View):
    """
    View which handles the upload of a csv file containing the athelte data
    """

    def post(self, request, *args, **kwargs):
        """
        Post Method
        :param request:
        :param args:
        :return:
        """
        # Get the form
        form = AthleteCSVImportForm(request.POST, request.FILES)

        # Check if the form is valid
        if form.is_valid():
            # Validate the file
            file = request.FILES['file']

            # Is file > 5 MByte ?
            if file.size > 5242880:
                return HttpResponseBadRequest(_("The given file is to big to import"))

            # Start the import
            try:
                conv_file = TextIOWrapper(file.file, encoding="UTF-8")
                import_athlete_csv(conv_file)
            except Exception as ex:
                return HttpResponseBadRequest(str(ex))
        else:
            return HttpResponseBadRequest(_("The given file is not valid"))

        return HttpResponse()
