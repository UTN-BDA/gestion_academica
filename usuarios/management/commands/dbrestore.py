import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Restore database from a backup file'

    def add_arguments(self, parser):
        parser.add_argument('backup_file', type=str, help='Path to the backup file')

    def handle(self, *args, **kwargs):
        backup_file = kwargs['backup_file']
        cmd = [
            'pg_restore',
            '--clean',
            '--dbname=postgresql://user:password@db:5432/main_db',
            backup_file,
        ]
        try:
            subprocess.run(cmd, check=True)
            self.stdout.write(self.style.SUCCESS('Database restored successfully.'))
        except subprocess.CalledProcessError as e:
            self.stderr.write(f'Error restoring database: {e}')