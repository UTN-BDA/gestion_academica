from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(dni='admin').exists():
            User.objects.create_superuser(
                dni='admin',
                email='admin@admin.com',
                password='admin',
                first_name='admin',
                last_name='admin'
            )
            self.stdout.write(self.style.SUCCESS('Usuario admin creado.'))
        else:
            self.stdout.write('El usuario admin ya existe.')
