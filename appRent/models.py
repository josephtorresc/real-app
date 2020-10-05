from django.db import models
from django.contrib.auth.models import User

from appApartment.models import Apartment

# Create your models here.

# clase de información de acompañantes
class Resident(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre(s)')
    surname = models.CharField(max_length=50, verbose_name='Apellido(s)')
    rut = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name='Número de rut')

    class Meta:
        ordering = ['id']
        verbose_name = 'Resident'
        verbose_name_plural = 'Residents'
        db_table = 'resident'

    def __str__(self):
        return '{}-{}'.format(self.name, self.surname)

# clase de estado de arriendo
class RentState(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        ordering = ['id']
        verbose_name = 'Rent State'
        verbose_name_plural = 'Rents States'
        db_table = 'rent_state'

    def __str__(self):
        return '{}'.format(self.name)


# Clase de administración de arriendos
class Rent(models.Model):
    code = models.CharField(max_length=50, verbose_name='Código')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Departamento')
    check_in_date = models.DateField(verbose_name="Fecha de CheckIn")
    check_out_date = models.DateField(verbose_name="Fecha de CheckOut")
    booking_payment = models.PositiveIntegerField(verbose_name="Pago de reserva")
    total_value = models.PositiveIntegerField(verbose_name="Valor total de reserva")
    state = models.ForeignKey(RentState, on_delete=models.CASCADE, verbose_name='Estado de la Reserva')
    registration_date = models.DateField(auto_now_add=False, verbose_name="Fecha de Registro")
    is_active = models.BooleanField(default=True, verbose_name='¿El registro está activo?')
    user = models.ManyToManyField(User, through='RentUser', verbose_name='Usuarios')
    resident = models.ManyToManyField(Resident, through='RentResident', verbose_name='Huespedes')

    class Meta:
        ordering = ['id']
        verbose_name = 'Rent'
        verbose_name_plural = 'Rents'
        db_table = 'rent'

    def __str__(self):
        return '{}-{}'.format(self.code, self.apartment.code)


# Clases para tablas intemedias de relaciones m2m
class RentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, verbose_name='Arriendo')
    is_employee = models.BooleanField(default=False, verbose_name='¿Es funcionario?')
    is_client = models.BooleanField(default=False, verbose_name='¿Es cliente?')

    class Meta:
        ordering = ['id']
        verbose_name = 'Rent User'
        verbose_name_plural = 'Rents Users'
        db_table = 'rent_user'

    def __str__(self):
        return '{}-{}'.format(self.rent.code, self.user.username)


class RentResident(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, verbose_name='Huesped')
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, verbose_name='Arriendo')
    is_active = models.BooleanField(default=True, verbose_name='¿Registro activo?')

    class Meta:
        ordering = ['id']
        verbose_name = 'Rent Resident'
        verbose_name_plural = 'Rents Residents'
        db_table = 'rent_resident'

    def __str__(self):
        return '{}-{}'.format(self.rent.code, self.resident.name)
