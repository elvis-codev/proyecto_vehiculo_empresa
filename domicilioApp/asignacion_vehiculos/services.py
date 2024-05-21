from asignacion_vehiculos.models import Vehicle, Driver, AccountingRegistry


def create_vehicle(registration_plate, brand, model, year, active):
    vehicle = Vehicle(
        registration_plate=registration_plate,
        brand=brand,
        model=model,
        year=year,
        active=active,
    )
    vehicle.save()
    return vehicle


def get_vehicle(registration_plate):
    return Vehicle.objects.get(registration_plate=registration_plate)


def create_driver(rut, name, last_name, active):
    driver = Driver(rut=rut, name=name, last_name=last_name, active=active)
    driver.save()
    return driver


def get_driver(rut):
    return Driver.objects.get(rut=rut)


def create_accounting_registry(vehicle, date_of_purchase, price):
    accounting_registry = AccountingRegistry(
        vehicle=vehicle, date_of_purchase=date_of_purchase, price=price
    )
    accounting_registry.save()
    return accounting_registry


def disable_driver(driver):
    driver.active = False
    driver.save()
    return driver


def disable_vehicle(vehicle):
    vehicle.active = False
    vehicle.save()
    return vehicle


def enable_driver(driver):
    driver.active = True
    driver.save()
    return driver


def enable_vehicle(vehicle):
    vehicle.active = True
    vehicle.save()
    return vehicle


def asignar_driver_a_vehicle(driver, vehicle):
    vehicle.driver = driver
    vehicle.save()
    driver.save()


def assign_driver_to_vehicle():
    vehicles = Vehicle.objects.all()
    for v in vehicles:
        print(
            f"Vehicle:{v.registration_plate}/{v.brand}/{v.model}/"
            + f"{v.year}/active:{v.active}"
        )
        if hasattr(v, "driver"):
            print(
                f"\tDriver[{v.driver.rut}]:{v.driver.name} "
                + f"{v.driver.last_name}/active:{v.driver.active}"
            )
        if hasattr(v, "contabilidad"):
            print(
                f"\tContabilidad:[{v.contabilidad.id}]:date_of_purchase:"
                + f"{v.contabilidad.date_of_purchase}/price:{v.contabilidad.price}"
            )
