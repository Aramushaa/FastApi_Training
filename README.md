# FastAPI Training Project

This repository contains a training project built to learn and demonstrate the use of **FastAPI** for building robust REST APIs.

## 🚀 Technologies & Concepts Covered

This project serves as a hands-on implementation of the following technologies and concepts:

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **PostgreSQL**: An advanced, enterprise-class, and open-source relational database system used as the primary data store.
- **SQLAlchemy**: The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **Docker**: Used for containerizing the application and database, ensuring consistency across different development and deployment environments.
- **CI/CD**: Continuous Integration and Continuous Deployment pipelines implemented to automate testing and deployment processes.
- **Pydantic**: Used extensively for data validation, serialization, and settings management via Python type annotations.
- **Modular Routing**: Structuring the API using FastAPI routers (e.g., for Users and Posts) to keep code organized and maintainable.

## 📂 Project Structure

- `app/`: Contains the core application code.
  - `main.py`: The entry point for the FastAPI application, containing the main App instance and DB connections.
  - `models.py`: SQLAlchemy database models representing tables.
  - `schemas.py`: Pydantic schemas for handling incoming request payloads and outgoing response structures.
  - `database.py`: Database connection configuration and session management.
  - `routers/`: Contains specific API route handlers (`user.py`, `post.py`).

## ⚙️ Getting Started

1. Set up your Python virtual environment (`venv`) and install the required dependencies.
2. Ensure you have a running instance of PostgreSQL. Update the connection credentials in your source code or securely via environment variables.
3. Start the application using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Navigate to `http://127.0.0.1:8000/docs` in your browser to interact with the auto-generated Swagger UI documentation.

## 📝 Note

This project is intended for educational purposes to explore and train on modern Python backend web development, containerization, database management, and automated workflows.
