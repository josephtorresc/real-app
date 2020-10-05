from django.db import models


# Create your models here.

# Clase de Tipos de Medio de Pago
class PymentType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Pyment Type'
        verbose_name_plural = 'Pyments Type'
        db_table = 'pyment_type'

    def __str__(self):
        return '{}'.format(self.name)


# Clases de Registro de Pagos
class RentPyment(models.Model):
    date_pyment = models.DateField(auto_now=True, verbose_name='Fecha de acción de pago')
    register_pyment = models.DateField(auto_now_add=True, verbose_name='Fecha de creación de registro')
    amount = models.PositiveIntegerField(verbose_name='Monto pagado')
    rent = models.ForeignKey("appRent.Rent", verbose_name="Arriendo", on_delete=models.CASCADE)
    pyment_type = models.ForeignKey(PymentType, verbose_name="Medio de pago", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Rent Pyment'
        verbose_name_plural = 'Rent Pyments'
        db_table = 'rent_pyment'

    def __str__(self):
        return '{}-{}'.format(self.rent,self.amount)


class ServicePyment(models.Model):
    date_pyment = models.DateField(auto_now=True, verbose_name='Fecha de acción de pago')
    register_pyment = models.DateField(auto_now_add=True, verbose_name='Fecha de creación de registro')
    amount = models.PositiveIntegerField(verbose_name='Monto pagado')
    service = models.ForeignKey("appExtraService.ServiceScheduled", verbose_name="Servicio", on_delete=models.CASCADE)
    pyment_type = models.ForeignKey(PymentType, verbose_name="Medio de pago", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Service Pyment'
        verbose_name_plural = 'Service Pyments'
        db_table = 'service_pyment'

    def __str__(self):
        return '{}-{}'.format(self.service,self.amount)


class AptCost(models.Model):
    date_action = models.DateField(auto_now=True, verbose_name='Fecha de acción de pago')
    register_action = models.DateField(auto_now_add=True, verbose_name='Fecha de creación de registro')
    amount = models.PositiveIntegerField(verbose_name='Monto pagado')
    apartment = models.ForeignKey("appApartment.Apartment", verbose_name="Departamento", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartment Cost'
        verbose_name_plural = 'Apartment Costs'
        db_table = 'apt_cost'

    def __str__(self):
        return '{}-{}'.format(self.apartment,self.amount)


class AptCostDescription(models.Model):
    description = models.TextField(verbose_name='Descripción del Gasto')
    apt_cost = models.OneToOneField(AptCost, on_delete=models.CASCADE, verbose_name='Registro de Costo')

    class Meta:
        ordering = ['id']
        verbose_name = 'Apartmen Cost Description'
        verbose_name_plural = 'Apartment Cost Descriptions'
        db_table = 'apt_cost_clob'

    def __str__(self):
        return '{}'.format(self.apt_cost)
