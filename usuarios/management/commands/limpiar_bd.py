from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction

class Command(BaseCommand):
    help = 'Elimina todos los datos de la base de datos'

    def handle(self, *args, **options):
        with transaction.atomic():
            for model in apps.get_models():
                model.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Base de datos vaciada.'))