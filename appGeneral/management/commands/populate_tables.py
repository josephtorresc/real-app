from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps
import csv
import os

from appApartment.models import Country, Region, Commune

class Command(BaseCommand):
    help = "Creación de datos iniciales para proyecto RealApp"

    def handle(self, *args, **options):
        list_initial_data = (
            ('country','appApartment','country'),
            ('region','appApartment','region'),
            ('commune','appApartment','commune'),
            ('type_bed','appApartment','typebed'),
            ('apt_state','appApartment','aptstate'),
            ('inventory_state','appApartment','inventorystate'),
            ('service','appApartment','service'),
            ('rent_state','appRent','rentstate'),
            ('user_type','appUser','usertype'),
            ('vehicle','appExtraService','vehicle'),
            ('pyment_type','appFinance','pymenttype'),
        )
        
        try:
            for tuple_data in list_initial_data: 
                message = insert_data(tuple_data[0],tuple_data[1],tuple_data[2])
                self.stdout.write(self.style.SUCCESS(message))
        except:
            self.stdout.write(self.style.ERROR(message))
            
def insert_data(csv_name, app_name, model_name):
    file_path = settings.BASE_DIR / os.path.normcase('appGeneral/csv_initial_data/{}.csv'.format(csv_name))
    model_object = apps.get_model(app_name, model_name)

    with open(file_path, 'r', encoding='utf-8') as data:
        list_data = list(csv.DictReader(data))

    message = ''
    if model_object.objects.all().exists():
        message = 'OK: Ya existen registros en el modelo {}'.format(model_object.__name__)
    else:
        if model_name == 'region':
            for row in list_data:
                row['country'] = Country.objects.get(name=row.pop('fk_country_name'))

        elif model_name == 'commune':
            for row in list_data:
                row['region'] = Region.objects.get(name=row.pop('fk_region_name'))

        for row in list_data:
            model_object.objects.create(**row)

        message = 'DONE: {}.{} registrados'.format(app_name, model_name)

    return message
