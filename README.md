# TalentSphere

TalentSphere is a career development platform for high school students, college students, and working professionals.

The project provides role-specific profiles, dashboards, assessments, career development tools, and career guidance features.

## Project Structure

- frontend/ - React and TypeScript frontend
- backend/ - FastAPI backend
- .gitignore - Git ignore rules
- README.md - Project documentation

## Frontend

Technologies:
- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Lucide React

Run the frontend:

    cd frontend
    npm ci
    npm run dev

Production build:

    npm run build

## Backend

Technologies:
- Python
- FastAPI
- SQLAlchemy
- Alembic
- JWT Authentication
- SQLite

Run the backend:

    cd backend
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.lock
    python -m alembic upgrade head
    uvicorn app.main:app --reload

## User Categories

- High School Student
- College Student
- Working Professional

## Current Development

The project contains role-specific frontend modules and a FastAPI backend with authentication, profile, dashboard, and assessment functionality.

Frontend-to-backend integration and final module cleanup are being completed incrementally.

## Development Principles

- Clear frontend and backend separation
- Modular and readable code
- Secure backend authentication
- Minimal duplicate and unused code
- Maintainable structure for future development

## Developed By

Vishal Kumar

B.Tech Computer Science and Engineering

## Purpose

Developed as an educational and internship project.
