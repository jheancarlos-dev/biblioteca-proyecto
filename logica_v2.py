from datetime import date, timedelta


class BibliotecaService:
    DIAS_PRESTAMO_ESTUDIANTE = 7
    DIAS_PRESTAMO_OTROS_USUARIOS = 15
    MULTA_POR_DIA_POR_LIBRO = 0.50

    def calcular_prestamo(self, tipo_usuario, dias_retraso, cantidad_libros):
        if dias_retraso < 0:
            raise ValueError("dias_retraso no puede ser negativo")
        if cantidad_libros < 0:
            raise ValueError("cantidad_libros no puede ser negativo")

        if tipo_usuario == "estudiante":
            plazo_prestamo_en_dias = self.DIAS_PRESTAMO_ESTUDIANTE
        else:
            plazo_prestamo_en_dias = self.DIAS_PRESTAMO_OTROS_USUARIOS

        monto_total_multa = (
            dias_retraso * cantidad_libros * self.MULTA_POR_DIA_POR_LIBRO
        )

        fecha_limite_devolucion = date.today() + timedelta(
            days=plazo_prestamo_en_dias
        )

        return monto_total_multa, fecha_limite_devolucion
