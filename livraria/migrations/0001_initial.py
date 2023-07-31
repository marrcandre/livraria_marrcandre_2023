# Generated by Django 4.2.3 on 2023-07-04 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autor",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
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
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Editora",
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
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
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
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True
                    ),
                ),
                (
                    "autores",
                    models.ManyToManyField(related_name="livros", to="livraria.autor"),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="livraria.categoria",
                    ),
                ),
                (
                    "editora",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="livraria.editora",
                    ),
                ),
            ],
        ),
    ]
