from django.contrib.auth.mixins import AccessMixin


class AthletePermissionRequiredMixin(AccessMixin):
    """
    Mixin which verifies the user has at least the athlete right
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(AthletePermissionRequiredMixin, self).dispatch(request, *args, **kwargs)