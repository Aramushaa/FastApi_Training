# FastAPI Social Media API (Learning Project)

This repository is my hands-on practice project while following a long-form FastAPI course.

The goal is to build a complete social-media-style backend API where users can:
- register and authenticate
- create/read/update/delete posts
- (next) like posts
- (next) add testing, deployment, Docker, and CI/CD

## Course Context

I am building this project based on a FastAPI course focused on:
- API design fundamentals (routes, schemas, validation, serialization/deserialization)
- SQL fundamentals with PostgreSQL
- database integration with raw SQL and SQLAlchemy ORM
- authentication and authorization
- testing with `pytest`
- deployment (Ubuntu + Heroku)
- Dockerization
- CI/CD with GitHub Actions

The course is split into two videos due to YouTube length limits.

## Current Implementation Status

Implemented in this repository right now:
- FastAPI app bootstrapped with modular routers
- PostgreSQL connection configured via environment variables
- SQLAlchemy models for `User` and `Post`
- password hashing with `passlib`/bcrypt
- JWT access token creation and validation
- login endpoint using OAuth2 password flow
- user registration and user lookup endpoints
- protected post CRUD endpoints with owner-only access control
- filtering/pagination on post list (`limit`, `skip`, `search`)

Planned but not yet implemented in this repo:
- likes feature
- test suite (`pytest`)
- Docker setup
- deployment scripts/workflows
- CI/CD pipeline configuration

## API Endpoints (Current)

- `GET /` - health/welcome route
- `POST /users/` - create user
- `GET /users/{id}` - get user by id
- `POST /login/` - authenticate and receive JWT token
- `GET /posts/` - list current user's posts (`limit`, `skip`, `search`)
- `POST /posts/` - create post (authenticated)
- `GET /posts/{id}` - get post by id (owner only)
- `PUT /posts/{id}` - update post (owner only)
- `DELETE /posts/{id}` - delete post (owner only)

## Project Structure

- `app/main.py` - app entrypoint and router registration
- `app/config.py` - settings loaded from `.env` via `pydantic-settings`
- `app/database.py` - SQLAlchemy engine/session setup
- `app/models.py` - ORM models (`User`, `Post`)
- `app/schemas.py` - request/response schemas
- `app/utils.py` - password hash/verify helpers
- `app/oauth2.py` - JWT + current-user dependency
- `app/routers/user.py` - user routes
- `app/routers/auth.py` - auth/login routes
- `app/routers/post.py` - post routes

## Environment Variables

Create a `.env` file with:

```env
database_hostname=localhost
database_port=5432
database_name=Fastapi
database_username=postgres
database_password=your_password
secret_key=your_secret_key
algorithm=HS256
access_token_expire_minutes=30
```

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg pydantic-settings passlib[bcrypt] python-jose[cryptography] email-validator python-multipart
```

3. Start the API:

```bash
uvicorn app.main:app --reload
```

4. Open Swagger docs:

- `http://127.0.0.1:8000/docs`

## Notes

- Database tables are currently created automatically from SQLAlchemy models on app startup (`Base.metadata.create_all(...)`).
- This project is for learning and will continue to evolve as I progress through the course.
