from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views import View

from AdminBackend.forms.forms import PasswordResetForm


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


class ResetUserPassword(View):
    """
    Called when a user reset is executed
    """

    def post(self, request, *args, **kwargs):
        """
        Post method
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """

        form = PasswordResetForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data["password"]
            user_id = form.cleaned_data["userId"]

            # Get the user object
            user = User.objects.get(pk=user_id)
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
        else:
            return HttpResponseBadRequest("The given data are not valid")

        return HttpResponse()
