from django.apps import AppConfig


class AccounterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounter'

    def ready(self):
        import accounter.signals 
