from django.apps import AppConfig


class KirishConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kirish'
    
    def ready(self):
        import kirish.signals
