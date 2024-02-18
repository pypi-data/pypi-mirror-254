from django.apps import AppConfig


class TenanetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tenanet"

    def ready(self):
        from tenanet import signals  # noqa
