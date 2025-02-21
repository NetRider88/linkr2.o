from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Test database connection'

    def handle(self, *args, **options):
        try:
            db_conn = connections['default']
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('Successfully connected to PostgreSQL database'))
        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f'Could not connect to PostgreSQL database: {e}')) 