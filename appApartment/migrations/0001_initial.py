# Generated by Django 3.1.1 on 2020-10-02 21:05

import appApartment.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Código')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('daily_price', models.PositiveIntegerField(verbose_name='Valor diario')),
                ('address', models.CharField(max_length=300, verbose_name='Dirección')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿El registro está activo?')),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
                'db_table': 'apartment',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Apartment State',
                'verbose_name_plural': 'Apartment States',
                'db_table': 'apt_state',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HouseholdGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Household Goods',
                'verbose_name_plural': 'Household Goods',
                'db_table': 'household_goods',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InventoryState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Inventory State',
                'verbose_name_plural': 'Inventory States',
                'db_table': 'inventory_state',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'db_table': 'service',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeBed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('people_capacity', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Type of Bed',
                'verbose_name_plural': 'Types of Bed',
                'db_table': 'type_bed',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.country', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'db_table': 'region',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.region', verbose_name='Región')),
            ],
            options={
                'verbose_name': 'Commune',
                'verbose_name_plural': 'Communes',
                'db_table': 'commune',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Número de habitación')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.apartment', verbose_name='Departamento')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.service', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'Apartment Service',
                'verbose_name_plural': 'Apartments Services',
                'db_table': 'apt_service',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_picture', models.CharField(max_length=200, verbose_name='Nombre de la imágen')),
                ('picutre', models.FileField(max_length=200, upload_to=appApartment.models.picture_path, verbose_name='Foto')),
                ('front_picture', models.BooleanField(default=False, verbose_name='¿Corresponde a la foto inicial?')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.apartment', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Apartment Picture',
                'verbose_name_plural': 'Apartments Pictures',
                'db_table': 'apt_picture',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Precio')),
                ('description', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Descripción')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.apartment', verbose_name='Departamento')),
                ('household_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.householdgoods', verbose_name='Enser')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.inventorystate', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Apartment Inventorie',
                'verbose_name_plural': 'Apartments Inventories',
                'db_table': 'apt_inventory',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripción del departamento')),
                ('apartment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appApartment.apartment', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Apartment Description',
                'verbose_name_plural': 'Apartments Descriptions',
                'db_table': 'apt_clob',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AptBedroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_bedroom', models.PositiveSmallIntegerField(verbose_name='Número de habitación')),
                ('amount_bed', models.PositiveSmallIntegerField(verbose_name='Cantidad de camas')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.apartment', verbose_name='Departamento')),
                ('type_bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.typebed', verbose_name='Tipo de Cama')),
            ],
            options={
                'verbose_name': 'Apartment Bedroom',
                'verbose_name_plural': 'Apartments Bedrooms',
                'db_table': 'apt_bedroom',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='bedroom',
            field=models.ManyToManyField(through='appApartment.AptBedroom', to='appApartment.TypeBed', verbose_name='Habitaciones'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.commune', verbose_name='Comuna'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='inventory',
            field=models.ManyToManyField(through='appApartment.AptInventory', to='appApartment.HouseholdGoods', verbose_name='Inventario'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='service',
            field=models.ManyToManyField(through='appApartment.AptService', to='appApartment.Service', verbose_name='Servicios'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appApartment.aptstate', verbose_name='Estado'),
        ),
    ]
