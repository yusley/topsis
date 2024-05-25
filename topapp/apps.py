from django.apps import AppConfig


class TopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topapp'

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topapp'

    def ready(self):
        import topapp.signals