# Generated by Django 4.2.13 on 2024-06-12 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_remove_profile_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="account",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="account.account"
            ),
        ),
    ]