from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json

class Command(BaseCommand):
    help = 'Cargar usuarios iniciales desde un archivo JSON y cifrar contraseñas'

    def handle(self, *args, **options):
        file_path = 'sonbuenos/fixtures/initial_data.json'

        try:
            with open(file_path) as file:
                usuarios = json.load(file)

            for usuario_data in usuarios:
                username = usuario_data['fields']['username']
                raw_password = usuario_data['fields']['password']

                # Cifra la contraseña
                hashed_password = make_password(raw_password)

                # Crea el usuario en la base de datos si no existe
                user, created = User.objects.get_or_create(username=username, defaults={'password': hashed_password})

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Se ha creado el usuario: {username}'))
                else:
                    self.stdout.write(self.style.WARNING(f'El usuario {username} ya existe en la base de datos'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('No se encontró el archivo JSON de datos iniciales'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error al decodificar el archivo JSON'))
