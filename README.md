# dno-fastapi-async

A learning project to master **FastAPI** and best practices for Python project workflows.

## 🎯 Purpose

This project demonstrates:
- Building async APIs with FastAPI
- Proper project structure and organization
- Testing with pytest and coverage
- Code quality with ruff linting and formatting
- Task automation with taskipy

## 📋 Requirements

- Python >= 3.14, < 4.0
- Poetry (for dependency management)

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Run the development server:**
   ```bash
   poetry run task dev
   ```

3. **Run tests:**
   ```bash
   poetry run task test
   ```

## 📦 Available Commands

| Command | Description |
|---------|-------------|
| `poetry run task dev` | Start FastAPI development server |
| `poetry run task lint` | Run code linting checks |
| `poetry run task format` | Format code with ruff |
| `poetry run task test` | Run tests with coverage report |

## 📚 Project Structure

```
dno-fastapi-async/
├── dno_fastapi_async/
│   ├── app.py          # FastAPI application
│   ├── schema.py       # Pydantic models
│   └── __init__.py
├── tests/              # Test suite
│   └── dno_fastapi_async/
│       └── test_app.py
├── pyproject.toml      # Project configuration
└── README.md
```

## 🧪 Endpoints

- `GET /` - Home endpoint
- `GET /about` - About endpoint

## 📖 Learning Goals

- [ ] Async request handling
- [ ] Dependency injection
- [ ] Database integration
- [ ] Authentication & authorization
- [ ] Advanced validation
- [ ] API documentation

---

**Author:** Marilzon
