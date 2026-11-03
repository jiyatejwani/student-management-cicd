# Student Management System — Automated CI/CD Pipeline

A REST API for managing student records, built with Flask and shipped through a
fully automated CI/CD pipeline on GitHub Actions. Every push is automatically
linted, tested, built into a Docker image, and published to the GitHub
Container Registry.

## Features

- Full CRUD on student records (create, list, fetch, update, delete)
- Input validation with clear error responses
- Health-check endpoint
- Automated test suite (pytest)
- Containerized with Docker
- Continuous Integration + Continuous Deployment via GitHub Actions

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| Web framework | Flask |
| Production server | gunicorn |
| Testing | pytest |
| Linting | flake8 |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Registry | GitHub Container Registry (GHCR) |

## Project Structure

```
student-management-cicd/
├── app/
│   ├── __init__.py      # Flask application factory
│   ├── models.py        # Student model and data store
│   └── routes.py        # REST API endpoints
├── tests/
│   └── test_students.py # Automated test suite
├── .github/workflows/
│   └── ci-cd.yml        # CI/CD pipeline definition
├── Dockerfile           # Container build recipe
├── requirements.txt     # Python dependencies
├── pytest.ini           # Test configuration
└── wsgi.py              # Application entry point
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/students` | List all students |
| POST | `/students` | Add a new student |
| GET | `/students/<id>` | Get one student |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

## Running Locally

```
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
pip install -r requirements.txt
python wsgi.py
```

The API runs at http://localhost:5000.

## Running Tests

```
python -m pytest -v
```

## The CI/CD Pipeline

Defined in `.github/workflows/ci-cd.yml`, it runs automatically on every push
and pull request to `main`:

1. **Lint and Test (CI)** — checks out the code, sets up Python 3.12, installs
   dependencies, runs flake8, and runs the pytest suite.
2. **Build and Publish Image (CD)** — runs only if the tests pass, builds the
   Docker image, and publishes it to the GitHub Container Registry.

A single `git push` automatically verifies, builds, and ships the application.

## Docker

```
docker build -t student-management .
docker run -p 5000:5000 student-management
```

## Live Deployment

Deployed at: <ADD YOUR LIVE URL HERE AFTER DEPLOYING>

## What I Learned

<Write 3-4 sentences in your own words: what CI/CD means, why automating tests
and builds matters, and one thing that surprised you while building this.>

## Author

**<Your Name>** — <Registration Number>
B.Tech CSE (AI & ML), Manipal University Jaipur
