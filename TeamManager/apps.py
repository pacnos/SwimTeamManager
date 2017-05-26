from django.apps import AppConfig


class TeammanagerConfig(AppConfig):
    name = 'TeamManager'

    def ready(self):
        import TeamManager.signals
