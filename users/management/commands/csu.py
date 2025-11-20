from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Женя',
            last_name='Евстратьев',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()