# Generated by Django 4.2.4 on 2023-08-14 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Concert",
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
                ("name", models.CharField(max_length=64)),
                (
                    "description",
                    models.TextField(blank=True, max_length=256, null=True),
                ),
                ("starts_at", models.DateTimeField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("tickets_left", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="ConcertCategory",
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
                ("name", models.CharField(max_length=64)),
                (
                    "description",
                    models.TextField(blank=True, max_length=256, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Venue",
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
                ("name", models.CharField(max_length=64)),
                (
                    "description",
                    models.TextField(blank=True, max_length=256, null=True),
                ),
                ("address", models.CharField(max_length=256, unique=True)),
                ("capacity", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("customer_full_name", models.CharField(max_length=64)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("CC", "Credit card"),
                            ("DC", "Debit card"),
                            ("ET", "Ethereum"),
                            ("BC", "Bitcoin"),
                        ],
                        default="CC",
                        max_length=2,
                    ),
                ),
                ("paid_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "concert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tickets.concert",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="concert",
            name="categories",
            field=models.ManyToManyField(to="tickets.concertcategory"),
        ),
        migrations.AddField(
            model_name="concert",
            name="venue",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tickets.venue",
            ),
        ),
    ]
