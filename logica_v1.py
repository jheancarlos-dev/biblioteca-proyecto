from datetime import date, timedelta


def calcular_prestamo(tipo_usuario, dias_retraso, cantidad_libros):
    if tipo_usuario == "estudiante":
        dias_prestamo = 7
    else:
        dias_prestamo = 15

    monto_multa = dias_retraso * cantidad_libros * 0.50

    fecha_devolucion = date.today() + timedelta(days=dias_prestamo)

    return monto_multa, fecha_devolucion
