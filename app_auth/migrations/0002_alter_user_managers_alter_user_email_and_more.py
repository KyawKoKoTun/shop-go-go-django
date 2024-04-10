# Generated by Django 5.0.1 on 2024-04-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=256),
        ),
    ]
