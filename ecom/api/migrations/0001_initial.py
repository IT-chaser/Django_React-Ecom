from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def send_data(apps, schema_editor):
        user = CustomUser(
            name="Asad",
            email="asad@email.com",
            is_staff=True,
            is_superuser=True,
            phone='123456789',
            gender="male"
        )

        user.set_password("123456")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(send_data),
    ]