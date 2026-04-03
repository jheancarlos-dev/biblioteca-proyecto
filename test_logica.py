from datetime import date, timedelta
from unittest import mock

import pytest

from logica_v3 import (
    BibliotecaService,
    PoliticaDocente,
    PoliticaEstudiante,
)


@pytest.fixture
def fecha_hoy_fija() -> date:
    return date(2026, 4, 3)


def test_estudiante_recibe_siete_dias_de_prestamo(fecha_hoy_fija: date) -> None:
    with mock.patch("logica_v3.date") as fecha_modulo:
        fecha_modulo.today.return_value = fecha_hoy_fija
        servicio = BibliotecaService(PoliticaEstudiante())
        _, fecha_limite = servicio.calcular_prestamo(0, 1)

    assert fecha_limite == fecha_hoy_fija + timedelta(days=7)


def test_docente_recibe_quince_dias_de_prestamo(fecha_hoy_fija: date) -> None:
    with mock.patch("logica_v3.date") as fecha_modulo:
        fecha_modulo.today.return_value = fecha_hoy_fija
        servicio = BibliotecaService(PoliticaDocente())
        _, fecha_limite = servicio.calcular_prestamo(0, 1)

    assert fecha_limite == fecha_hoy_fija + timedelta(days=15)


def test_multa_estudiante_dos_dias_tres_libros_es_tres_pesos() -> None:
    servicio = BibliotecaService(PoliticaEstudiante())
    monto_multa, _ = servicio.calcular_prestamo(2, 3)

    assert monto_multa == pytest.approx(3.0)


def test_lanza_valueerror_si_dias_retraso_negativo() -> None:
    servicio = BibliotecaService(PoliticaEstudiante())

    with pytest.raises(ValueError, match="dias_retraso"):
        servicio.calcular_prestamo(-1, 1)


def test_lanza_valueerror_si_cantidad_libros_es_cero() -> None:
    servicio = BibliotecaService(PoliticaEstudiante())

    with pytest.raises(ValueError, match="cantidad_libros"):
        servicio.calcular_prestamo(0, 0)


def test_lanza_valueerror_si_cantidad_libros_negativa() -> None:
    servicio = BibliotecaService(PoliticaDocente())

    with pytest.raises(ValueError, match="cantidad_libros"):
        servicio.calcular_prestamo(0, -1)
