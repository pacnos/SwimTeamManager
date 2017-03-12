from datetime import date


def json_serial(obj):
    """
    JSON serializer for objects not serializable by default json code
    """

    if isinstance(obj, date):
        return obj.strftime("%d.%m.%Y")

    raise TypeError("Type not serializable")
