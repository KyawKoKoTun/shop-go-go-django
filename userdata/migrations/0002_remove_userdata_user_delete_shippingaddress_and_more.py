# Generated by Django 5.0.1 on 2024-04-05 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userdata", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdata",
            name="user",
        ),
        migrations.DeleteModel(
            name="ShippingAddress",
        ),
        migrations.DeleteModel(
            name="UserData",
        ),
    ]
