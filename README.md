# 📚 Sistema de Gestión de Préstamos - Biblioteca Central "Mario Vargas Llosa"

> Proyecto académico para el curso de **Construcción de Software**  
> Enfoque: Clean Code, Refactorización, Manejo de Excepciones y Metodologías Ágiles.

## 🎯 Descripción
Aplicación web sencilla que automatiza el cálculo de fechas de devolución y multas por retraso en el préstamo de libros. Desarrollada aplicando principios de ingeniería de software y asistida por inteligencia artificial generativa.

## 🛠️ Tecnologías y Buenas Prácticas
| Categoría | Herramienta / Enfoque |
|-----------|----------------------|
| **Lenguaje** | Python 3.x |
| **Framework Web** | Flask |
| **IA Generativa** | Cursor (refactorización guiada) |
| **Patrones de Diseño** | Strategy + Inyección de Dependencias |
| **Calidad de Código** | Clean Code, SOLID, PEP 8 |
| **Pruebas** | pytest + unittest.mock |
| **Manejo de Errores** | Validación temprana con `ValueError` |

## 🔄 Evolución del Código (Iteraciones)
| Archivo | Descripción |
|---------|-------------|
| `logica_v1.py` | Versión inicial procedimental (números mágicos, sin validaciones) |
| `logica_v2.py` | Refactorización: clase `BibliotecaService`, constantes, validaciones básicas |
| `logica_v3.py` | Arquitectura final: Patrón Strategy, tipado explícito, desacoplamiento total |
| `test_logica.py` | Pruebas unitarias automatizadas con casos límite y mocking de fechas |

## ⚙️ Instalación y Uso
```bash
# 1. Clonar el repositorio
git clone https://github.com/jheancarlos-dev/biblioteca-proyecto.git
cd biblioteca-proyecto

# 2. Instalar dependencias
pip install flask pytest

# 3. Ejecutar la aplicación
python app.py

# 4. Acceder en el navegador
# http://127.0.0.1:5000

# 5. (Opcional) Ejecutar pruebas
pytest test_logica.py -v
