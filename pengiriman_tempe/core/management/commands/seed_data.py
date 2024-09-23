from django.core.management.base import BaseCommand
from django_seed import Seed
from core.models import Tempe, PesananTempe, Pengiriman
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with dummy data"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        # Seed 10 Tempe data
        seeder.add_entity(Tempe, 10, {
            'nama_tempe': lambda x: seeder.faker.name(),
            'harga': lambda x: seeder.faker.random_number(digits=5),
            'deskripsi': lambda x: seeder.faker.text(),
        })

        # Seed 10 User data (required for PesananTempe)
        seeder.add_entity(User, 10, {
            'username': lambda x: seeder.faker.user_name(),
            'email': lambda x: seeder.faker.email(),
        })

        # Seed 10 PesananTempe data
        seeder.add_entity(PesananTempe, 10, {
            'pengguna': lambda x: User.objects.order_by('?').first(),
            'tempe': lambda x: Tempe.objects.order_by('?').first(),
            'jumlah': lambda x: seeder.faker.random_int(min=1, max=5),
            'alamat_pengiriman': lambda x: seeder.faker.address(),
        })

        # Seed 10 Pengiriman data
        seeder.add_entity(Pengiriman, 10, {
            'pesanan': lambda x: PesananTempe.objects.order_by('?').first(),
            'status_pengiriman': lambda x: seeder.faker.random_element(elements=('Dikirim', 'Dalam Perjalanan', 'Selesai')),
            'tanggal_pengiriman': lambda x: seeder.faker.date_this_year(),
        })

        # Execute the seeder
        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS('Database has been seeded.'))
