# 🧪 QA-API-Tests

Repositorio de pruebas manuales y automatizadas sobre la API pública JSONPlaceholder.

---

## 📂 Estructura del proyecto

QA-API-Tests/
- Automation/
    - test_api_jsonplaceholder.py ✅
    - __init__.py
- Manual-API-TestCases/
    - QA-API-TestCases.xlsx
    - QA-API-TestCases_JSONPlaceholder.xlsx
- .gitignore
- README.md

---

## 🧰 Herramientas utilizadas

- Postman (pruebas manuales)
- Python + Unittest (automatización)
- API pública: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- Git + GitHub

---

## 📌 Descripción de los tests automatizados

Los siguientes métodos fueron validados contra JSONPlaceholder usando `unittest`:

| Test ID | Método | Endpoint                                       | Estado esperado | Estado real | Estado |
|---------|--------|------------------------------------------------|------------------|-------------|--------|
| 1       | GET    | `/posts`                                       | 200              | 200         | ✅     |
| 2       | GET    | `/posts/1`                                     | 200              | 200         | ✅     |
| 3       | POST   | `/posts`                                       | 201              | 201         | ✅     |
| 4       | PUT    | `/posts/1`                                     | 200              | 200         | ✅     |
| 5       | PATCH  | `/posts/1`                                     | 200              | 200         | ✅     |
| 6       | DELETE | `/posts/1`                                     | 200              | 200         | ✅     |

---

## 📊 Casos de prueba manuales

🗂️ Archivo: `QA-API-TestCases_JSONPlaceholder.xlsx`  
Contiene los mismos 6 tests validados manualmente con Postman antes de su automatización. Incluye:

- Métodos: GET, POST, PUT, PATCH, DELETE
- Estructura organizada con campos: ID, Método, Endpoint, Body, Resultado Esperado, Resultado Real, Estado

---

## 🚀 Estado del proyecto

✅ Etapa finalizada  
🧩 Tests API manuales + automatizados completos  
📁 Estructura organizada para futuros proyectos y CI/CD

---

## 📌 Próximo paso: CI/CD + GitHub Actions
El siguiente arco de la temporada 3 consistirá en crear un repositorio independiente para automatizar la ejecución de tests en cada push.

---
