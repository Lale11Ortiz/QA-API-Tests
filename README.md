##🧪 QA-API-Tests
Repositorio de pruebas manuales y automatizadas sobre la API pública JSONPlaceholder.

---

##📁 Estructura del proyecto

QA-API-Tests/
│
├── 📂 Automation
│   ├── test_api_jsonplaceholder.py                 # Tests automatizados con `unittest`
│   ├── 📂 pytest_tests
│   │   ├── test_jsonplaceholder_pytest.py         # Tests con `pytest`
│   │   └── conftest.py                            # Fixture compartida
│
├── 📂 Manual-API-TestCases
│   ├── QA-API-TestCases_JSONPlaceholder.xlsx      # Casos de prueba manuales
│   └── QA-API-TestCasesxlsx                       # Casos de prueba manuales
│
├── .gitignore                                     # Ignora archivos temporales, Allure, etc.
├── README.md                                      # Este archivo

---

##🧪 Tests Automatizados

✔️ Herramientas utilizadas:
- Python 3.13
- `unittest`
- `pytest`
- `requests`
- `Allure` para reporting
- `GitHub Actions` para CI/CD

---

##📋 Tests cubiertos (JSONPlaceholder API):

| ID | Método | Endpoint                                       | Estado |
|----|--------|------------------------------------------------|--------|
| 1  | GET    | `/posts`                                       | ✅     |
| 2  | GET    | `/posts/1`                                     | ✅     |
| 3  | POST   | `/posts`                                       | ✅     |
| 4  | PUT    | `/posts/1`                                     | ✅     |
| 5  | PATCH  | `/posts/1`                                     | ✅     |
| 6  | DELETE | `/posts/1`                                     | ✅     |

Todos los tests fueron implementados con `unittest` y duplicados con `pytest` para práctica avanzada y generación de reportes con Allure.

---

##📊 Reportes con Allure

Se utilizó `pytest + allure-pytest` para generar reportes detallados ejecutando:

```bash
pytest Automation/pytest_tests/test_jsonplaceholder_pytest.py --alluredir=allure-results
allure serve allure-results
El comando abre automáticamente el reporte HTML local en el navegador.

---

##🔁 CI/CD con GitHub Actions
El proyecto cuenta con un flujo de trabajo CI básico para ejecutar los tests automáticamente:

`.github/workflows/python-ci.yml`

- Corre en cada push y PR
- Verifica dependencias
- Ejecuta `unittest`
- Integra validación de calidad de código con `flake8`

---

##✍️🏽 Objetivo

Practicar de forma profesional la validación de APIs REST tanto en pruebas manuales como automatizadas, consolidando experiencia en:
- Gestión de ramas (`Git`)
- Buenas prácticas de estructuración de proyectos
- Automatización avanzada
- CI/CD y reportes