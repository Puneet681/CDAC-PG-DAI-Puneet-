# Generated by Django 4.1 on 2023-09-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("pid", models.CharField(max_length=20)),
                ("pname", models.CharField(max_length=100)),
                ("qty", models.IntegerField(null=True)),
                ("price", models.FloatField()),
            ],
            options={
                "db_table": "product",
            },
        ),
    ]
