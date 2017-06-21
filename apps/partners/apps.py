from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class PartnersConfig(AppConfig):
    name = 'partners'

    def ready(self):
        Partner = self.get_model('Partner')
        watson.register(Partner, adapter_cls=PageBaseSearchAdapter)
