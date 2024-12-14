from django.core.management.base import BaseCommand
from musicians.models import Musician, Band, Wilaya


class Command(BaseCommand):
    help = 'Seeds the database with initial data for musicians'

    def handle(self, *args, **options):
        if not Musician.objects.filter(email='admin@example.com').exists():
            Musician.objects.create_superuser('admin@example.com', 'Moudir', 'Drabki', 'toor')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))

        # Create Hamamat Band (idempotent)
        if not Band.objects.filter(name='Hamamat').exists():
            hamamat_band = Band.objects.create(name='Hamamat', phone_number='0123456789', wilaya=Wilaya.ORAN)
            self.stdout.write(self.style.SUCCESS('Successfully created Hamamat band.'))
        else:
            self.stdout.write(self.style.WARNING('Hamamat band already exists.'))

        # Create Musician (idempotent -  using email as a unique identifier)
        if not Musician.objects.filter(email='musician@example.com').exists():
            musician = Musician.objects.create(
                email='musician@example.com',
                first_name='Example',
                last_name='Musician',
                address='Oran Address',
                birth_date='1990-01-01',
                instrument='Derbouka',
                phone_number='9876543210',
                band=Band.objects.get(name='Hamamat') # Assuming you have a foreign key relationship
            )
            musician.set_password('your_password') # Set password separately (important for security)
            musician.save()
            self.stdout.write(self.style.SUCCESS('Successfully created musician.'))
        else:
            self.stdout.write(self.style.WARNING('Musician already exists.'))

