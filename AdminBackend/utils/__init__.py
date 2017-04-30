from django.contrib.auth.models import Group

AVAILABLE_RIGHT_GROUPS = (
    ("AT", "Athlete"),
    ("CO", "Coach"),
    ("ADMIN", "Admin")
)

AVAILABLE_GROUPS = {
    "AT": "Athlete",
    "CO": "Coach"
}


def get_group_key_for_user(user):
    """
    Returns the Group key for the given user
    :return: 
    """

    groups = user.groups.all()

    if len(groups) == 0:
        return "ADMIN"
    else:
        for key, value in AVAILABLE_GROUPS.iteritems():
            if groups[0] == value:
                return key

def set_group_for_user(user, group):
    """
    Sets the group for the given user
    :param user: 
    :return: 
    """

    user.groups.clear()
    if group == "AT" or group == "CO":
        group = Group.objects.get(name=AVAILABLE_GROUPS[group])
        user.groups.add(group)
    else:
        user.is_superuser = True