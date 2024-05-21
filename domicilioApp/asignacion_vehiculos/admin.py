from django.contrib import admin
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

from .models import Driver, Vehicle, AccountingRegistry

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    actions = ["export_to_csv", "export_to_pdf"]
    readonly_fields = ('created_at',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Conductores.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Nombre", "Apellido", "Activo", "Creado En", "Vehículo"])
        for driver in queryset:
            writer.writerow([
                driver.rut,
                driver.name,
                driver.last_name,
                driver.active,
                driver.created_at,
                driver.vehicle
            ])
        return response

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="Conductores.pdf"'
        p = canvas.Canvas(response)

        # Crear una lista para almacenar los datos de los conductores
        data = [["RUT", "Nombre", "Apellido", "Activo", "Creado En", "Vehículo"]]

        # Agregar los datos de los conductores a la lista
        for driver in queryset:
            data.append([
                driver.rut,
                driver.name,
                driver.last_name,
                driver.active,
                str(driver.created_at),  # Convertir a cadena si es necesario
                driver.vehicle
            ])

        # Crear una tabla con los datos
        table = Table(data)

        # Establecer el estilo de la tabla
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

        table.setStyle(style)

        # Dibujar la tabla en el lienzo
        table.wrapOn(p, 800, 600)
        table.drawOn(p, 72, 600)

        p.showPage()
        p.save()
        return response

    export_to_csv.short_description = "Exportar conductores seleccionados a CSV"
    export_to_pdf.short_description = "Exportar conductores seleccionados a PDF"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    actions = ["export_to_csv", "export_to_pdf"]
    readonly_fields = ('created_at',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Vehículos.csv"'
        writer = csv.writer(response)
        writer.writerow(
            ["Matrícula", "Marca", "Modelo", "Año", "Activo", "Creado en"]
        )
        for vehicle in queryset:
            writer.writerow(
                [
                    vehicle.registration_plate,
                    vehicle.brand,
                    vehicle.model,
                    vehicle.year,
                    vehicle.active,
                    vehicle.created_at,
                ]
            )
        return response

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="Vehículos.pdf"'
        p = canvas.Canvas(response)

        data = [["Matrícula", "Marca", "Modelo", "Año", "Activo", "Creado en"]]

        for vehicle in queryset:
            data.append([
                vehicle.registration_plate,
                vehicle.brand,
                vehicle.model,
                vehicle.year,
                vehicle.active,
                str(vehicle.created_at),  # Convertir a cadena si es necesario
            ])

        table = Table(data)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        table.setStyle(style)

        table.wrapOn(p, 800, 600)
        table.drawOn(p, 72, 600)

        p.showPage()
        p.save()
        return response

    export_to_csv.short_description = "Exportar vehículos seleccionados a CSV"
    export_to_pdf.short_description = "Exportar vehículos seleccionados a PDF"


@admin.register(AccountingRegistry)
class AccountingRegistryAdmin(admin.ModelAdmin):
    actions = ["export_to_csv", "export_to_pdf"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="registros_contables.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(["Fecha de Compra", "Precio", "Vehículo"])
        for accounting_registry in queryset:
            writer.writerow(
                [
                    accounting_registry.date_of_purchase,
                    accounting_registry.price,
                    accounting_registry.vehicle,
                ]
            )
        return response

    def export_to_pdf(self, request, queryset):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="Registros_Contables.pdf"'
        p = canvas.Canvas(response)

        data = [["Fecha de Compra", "Precio", "Vehículo"]]

        for accounting_registry in queryset:
            data.append([
                accounting_registry.date_of_purchase,
                accounting_registry.price,
                accounting_registry.vehicle,
            ])

        table = Table(data)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        table.setStyle(style)

        table.wrapOn(p, 800, 600)
        table.drawOn(p, 72, 600)

        p.showPage()
        p.save()
        return response

    export_to_csv.short_description = "Exportar registros contables seleccionados a CSV"
    export_to_pdf.short_description = "Exportar registros contables seleccionados a PDF"

