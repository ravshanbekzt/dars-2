import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Admin parolini environment variable orqali yangilash"

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")

        if not username or not password:
            self.stdout.write(
                self.style.ERROR(
                    "ADMIN_USERNAME yoki ADMIN_PASSWORD topilmadi."
                )
            )
            return

        User = get_user_model()

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
            self.style.SUCCESS("Admin paroli muvaffaqiyatli yangilandi.")
        )

















