from django.apps import AppConfig


class SocietyRegConfig(AppConfig):
    name = 'society_reg'
    def ready(self):
        import society_reg.signals