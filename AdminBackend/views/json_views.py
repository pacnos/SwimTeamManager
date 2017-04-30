from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views import View


class UserDeleteJSON(View):
    """
    Deletes an User
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
            user = User.objects.get(pk=self.args[0])
            user.delete()
        except ObjectDoesNotExist as ex:
            return HttpResponseBadRequest("Can't find user to delete")

        return HttpResponse()
