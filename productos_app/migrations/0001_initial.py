# Generated by Django 5.1.3 on 2024-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('calidad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=255)),
                ('id_sucursal', models.PositiveIntegerField()),
                ('id_provedor', models.PositiveIntegerField()),
            ],
        ),
    ]