from django.db import models

# Create your models here.

# Clases para administración de localidad de departamento
class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'country'

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='País')

    class Meta:
        ordering = ['id']
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        db_table = 'region'

    def __str__(self):
        return self.name

class Commune(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Región')

    class Meta:
        ordering = ['id']
        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'
        db_table = 'commune'

    def __str__(self):
        return self.name

# clases para administración de inventario
class InventoryState(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Inventory State'
        verbose_name_plural = 'Inventory States'
        db_table = 'inventory_state'

    def __str__(self):
        return self.name

class HouseholdGoods(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Household Goods'
        verbose_name_plural = 'Household Goods'
        db_table = 'household_goods'

    def __str__(self):
        return self.name

# clases para administrar habitaciones y capacidad de departamento
class TypeBed(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    people_capacity = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Type of Bed'
        verbose_name_plural = 'Types of Bed'
        db_table = 'type_bed'

    def __str__(self):
        return self.name

# Clase para administrar servicios básico de los departamentos
class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'service'

    def __str__(self):
        return self.name

# Clase para definir el estado del departamento
class AptState(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment State'
        verbose_name_plural = 'Apartment States'
        db_table = 'apt_state'

    def __str__(self):
        return self.name

# Clase para administrar departamento
class Apartment(models.Model):
    code = models.CharField(max_length=50, verbose_name='Código')
    title = models.CharField(max_length=50, verbose_name='Título')
    daily_price = models.PositiveIntegerField(verbose_name='Valor diario')
    address = models.CharField(max_length=300, verbose_name='Dirección')
    is_active = models.BooleanField(default=True, verbose_name='¿El registro está activo?')
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, verbose_name='Comuna')
    state = models.ForeignKey(AptState, on_delete=models.CASCADE, verbose_name='Estado')
    inventory = models.ManyToManyField(HouseholdGoods, through='AptInventory', verbose_name='Inventario')
    bedroom = models.ManyToManyField(TypeBed, through='AptBedroom', verbose_name='Habitaciones')
    service = models.ManyToManyField(Service, through='AptService', verbose_name='Servicios')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'
        db_table = 'apartment'

    def __str__(self):
        return self.title

# Clases para tablas intemedias de relaciones m2m
class AptInventory(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')
    household_goods = models.ForeignKey(HouseholdGoods, on_delete=models.CASCADE, verbose_name='Enser')
    state = models.ForeignKey(InventoryState, on_delete=models.CASCADE, verbose_name='Estado')
    amount = models.PositiveIntegerField(verbose_name='Precio')
    description = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name='Descripción')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Inventorie'
        verbose_name_plural = 'Apartments Inventories'
        db_table = 'apt_inventory'

    def __str__(self):
        return '{}-{}'.format(self.apartment.title, self.household_goods.name)


class AptBedroom(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')
    type_bed = models.ForeignKey(TypeBed, on_delete=models.CASCADE, verbose_name='Tipo de Cama')
    num_bedroom = models.PositiveSmallIntegerField(verbose_name='Número de habitación')
    amount_bed = models.PositiveSmallIntegerField(verbose_name='Cantidad de camas')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Bedroom'
        verbose_name_plural = 'Apartments Bedrooms'
        db_table = 'apt_bedroom'

    def __str__(self):
        return '{}-{}'.format(self.apartment.title, self.type_bed.name)


class AptService(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')
    description = models.CharField(max_length=100, verbose_name='Número de habitación')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Service'
        verbose_name_plural = 'Apartments Services'
        db_table = 'apt_service'

    def __str__(self):
        return '{}-{}'.format(self.apartment.title, self.type_bed.name)


# Clases de extención de información de Departamento
def picture_path(instance, document_name):
    folder_name = '{0}-{1}'.format(instance.apartment.code, instance.apartment.title)

    return '{0}/{1}'.format(folder_name, document_name)


class AptPicture(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')
    name_picture = models.CharField(max_length=200, verbose_name='Nombre de la imágen')
    picutre = models.FileField(upload_to=picture_path,  max_length=200, verbose_name='Foto')
    front_picture = models.BooleanField(default=False, verbose_name='¿Corresponde a la foto inicial?')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Picture'
        verbose_name_plural = 'Apartments Pictures'
        db_table = 'apt_picture'

    def __str__(self):
        return '{}'.format(self.apartment.title)


class AptDescription(models.Model):
    description = models.TextField(verbose_name='Descripción del departamento')
    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Description'
        verbose_name_plural = 'Apartments Descriptions'
        db_table = 'apt_clob'

    def __str__(self):
        return '{}'.format(self.apartment.title)
