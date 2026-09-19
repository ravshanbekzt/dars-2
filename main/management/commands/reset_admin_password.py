from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Admin parolini yangilash"

    def add_arguments(self, parser):
        parser.add_argument("username")
        parser.add_argument("password")

    def handle(self, *args, **options):
        User = get_user_model()

        username = options["username"]
        password = options["password"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Bunday foydalanuvchi topilmadi.")
            )
            return

        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS("Parol muvaffaqiyatli yangilandi.")
        )


















