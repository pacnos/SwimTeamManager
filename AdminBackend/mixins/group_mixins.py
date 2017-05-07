from django.contrib.auth.mixins import AccessMixin

from AdminBackend.models import TMUser


class AthletePermissionRequiredMixin(AccessMixin):
    """
    Mixin which verifies the user has at least the athlete right
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(AthletePermissionRequiredMixin, self).dispatch(request, *args, **kwargs)


class CoachPermissionRequiredMixin(AccessMixin):
    """
    Mixin which verifies the user has at least the coach right
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.tmuser.is_coach_or_admin():
            return self.handle_no_permission()
        return super(CoachPermissionRequiredMixin, self).dispatch(request, *args, **kwargs)


class AdminPermissionRequiredMixin(AccessMixin):
    """
    Mixin which verifies the user has at least the coach right
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.tmuser.is_admin():
            return self.handle_no_permission()
        return super(AdminPermissionRequiredMixin, self).dispatch(request, *args, **kwargs)
