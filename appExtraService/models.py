from django.db import models

# Create your models here.

# clase de vehiculo para los servicios extra
class Vehicle(models.Model):
    patent = models.CharField(max_length=8, verbose_name='Patente')
    capacity = models.PositiveSmallIntegerField(verbose_name='Capacidad de pasajeros')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    brand = models.CharField(max_length=50, verbose_name='Marca')
    description = models.CharField(max_length=200, null=True, blank=True, default='', verbose_name='Descripción')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        db_table = 'vehicle'

    def __str__(self):
        return '{}-{}'.format(self.brand, self.model)


# Clase de información de Tours disponibles
class Tour(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    price_per_person = models.PositiveSmallIntegerField(verbose_name='Precio por persona')
    is_active = models.BooleanField(default=True, verbose_name='¿El registro está activo?')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        db_table = 'tour'

    def __str__(self):
        return '{}'.format(self.name)

class TourDescription(models.Model):
    description = models.TextField(verbose_name='Descripción del Tour')
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, verbose_name='Tour')

    class Meta:
        ordering = ['id']
        verbose_name = 'Tour Description'
        verbose_name_plural = 'Tours Descriptions'
        db_table = 'tour_clob'

    def __str__(self):
        return '{}'.format(self.tour.name)


# Clase padre de agenda de servicio
class ServiceScheduled(models.Model):
    date_scheduled = models.DateTimeField(verbose_name="Fecha agendada")
    price = models.PositiveIntegerField(verbose_name="Valor de servicio")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehiculo asignado')
    is_active = models.BooleanField(default=True, verbose_name='¿El registro está activo?')

    class Meta:
        ordering = ['id']
        verbose_name = 'Service Scheduled'
        verbose_name_plural = 'Services Scheduleds'
        db_table = 'service_scheduled'

    def __str__(self):
        return '{}-{}'.format(self.date_scheduled, self.vehicle)

class ScheduledDescription(models.Model):
    description = models.TextField(verbose_name='Descripción del Servicio')
    scheduled = models.OneToOneField(ServiceScheduled, on_delete=models.CASCADE, verbose_name='Agenda de servicio')

    class Meta:
        ordering = ['id']
        verbose_name = 'scheduled description'
        verbose_name_plural = 'scheduled description'
        db_table = 'svc_scheduled_clob'

    def __str__(self):
        return '{}'.format(self.scheduled)


# Clases hijas que heredan de la agenda de servicio
class TourScheduled(ServiceScheduled):
    people_total = models.PositiveSmallIntegerField(verbose_name='Total de personas')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Tour')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Tour Scheduled'
        verbose_name_plural = 'Tours Scheduleds'
        db_table = 'tour_scheduled'

    def __str__(self):
        return '{}-{}'.format(self.date_scheduled, self.tour)

class TransportScheduled(ServiceScheduled):
    meeting_place = models.CharField(max_length=200, verbose_name='Lugar de encuentro')
    destination_place = models.CharField(max_length=200, verbose_name='Lugar de destino')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Transport Scheduled'
        verbose_name_plural = 'Transports Scheduleds'
        db_table = 'transport_scheduled'

    def __str__(self):
        return '{}-{}'.format(self.date_scheduled, self.meeting_place)
