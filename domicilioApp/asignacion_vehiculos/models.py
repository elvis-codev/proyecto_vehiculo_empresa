from django.db import models
from django.db.models import PROTECT
from django.utils import timezone


# Create your models here.
class Driver(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name="RUT")
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellido")
    active = models.BooleanField(default=False, verbose_name="Activo")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Creado en")
    vehicle = models.OneToOneField(
        "Vehicle",
        related_name="driver",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name="Vehículo"
    )

    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
        ordering = ["rut"]



class Vehicle(models.Model):
    registration_plate = models.CharField(max_length=6, primary_key=True, verbose_name="Placa de registro")
    brand = models.CharField(max_length=20, null=False, blank=False, verbose_name="Marca")
    model = models.CharField(max_length=20, null=False, blank=False, verbose_name="Modelo")
    year = models.DateField(null=False, blank=False, verbose_name="Año")
    active = models.BooleanField(default=False, verbose_name="Activo")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Creado en")

    def __str__(self):
        return self.registration_plate

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ["registration_plate"]



class AccountingRegistry(models.Model):
    date_of_purchase = models.DateField(null=False, blank=False, verbose_name="Fecha de Compra")
    price = models.FloatField(null=False, blank=False, verbose_name="Precio")
    vehicle = models.OneToOneField(
        "Vehicle", related_name="accounting_registry", on_delete=models.PROTECT, verbose_name="Vehículo"
    )

    def __str__(self):
        return self.vehicle.registration_plate

    class Meta:
        verbose_name = "Registro Contable"
        verbose_name_plural = "Registros Contables"
        ordering = ["date_of_purchase"]
