from flask import Flask, render_template, request

from logica_v3 import BibliotecaService, PoliticaDocente, PoliticaEstudiante

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/calcular")
def calcular():
    tipo_usuario = request.form.get("tipo_usuario", "")

    try:
        dias_retraso = int(request.form.get("dias_retraso", ""))
        cantidad_libros = int(request.form.get("cantidad_libros", ""))
    except ValueError:
        return render_template(
            "resultado.html",
            error="Introduce números enteros válidos en días de retraso y cantidad de libros.",
        )

    if tipo_usuario == "estudiante":
        politica = PoliticaEstudiante()
    elif tipo_usuario == "docente":
        politica = PoliticaDocente()
    else:
        return render_template(
            "resultado.html",
            error="El tipo de usuario no es válido. Elige estudiante o docente.",
        )

    servicio = BibliotecaService(politica)

    try:
        monto_multa, fecha_limite_devolucion = servicio.calcular_prestamo(
            dias_retraso, cantidad_libros
        )
    except ValueError as exc:
        mensaje = str(exc).strip() or "Los datos del formulario no son válidos."
        return render_template(
            "resultado.html",
            error=f"No se pudo calcular el préstamo: {mensaje}",
        )

    return render_template(
        "resultado.html",
        monto_multa=monto_multa,
        fecha_limite_devolucion=fecha_limite_devolucion,
        tipo_usuario=tipo_usuario,
    )


if __name__ == "__main__":
    app.run(debug=True)
