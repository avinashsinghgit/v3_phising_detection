# Generated by Django 4.1.4 on 2023-08-08 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phished_url", models.URLField()),
                ("email", models.EmailField(max_length=30)),
                ("comment", models.TextField(max_length=30)),
            ],
        ),
    ]
