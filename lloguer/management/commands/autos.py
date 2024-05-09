from django.core.management.base import BaseCommand
from faker import Faker
from faker_vehicle import VehicleProvider
from lloguer.models import Automobil

fake = Faker()
fake.add_provider(VehicleProvider)

class Command(BaseCommand):
    help = 'Genera datos falsos de coches'

    def handle(self, *args, **options):
        print("Generando datos falsos de coches...")

        # Generar 200 coches falsos
        for _ in range(200):
            marca = fake.vehicle_make()
            modelo = fake.vehicle_model()
            matricula = fake.license_plate()
            automovil = Automobil(marca=marca, model=modelo, matricula=matricula)
            automovil.save()

        print("Se han generado 200 coches falsos exitosamente.")
