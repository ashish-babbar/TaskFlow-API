# Task Tracker API

A small but "real" backend project: FastAPI + SQLAlchemy + JWT auth + rate limiting + tests.
This is meant as a template — swap "tasks" for whatever domain interests you (expenses, habits,
bookmarks) and the same architecture holds up.

## Run it

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs — FastAPI auto-generates interactive API docs, which is
genuinely useful to show in an interview or demo video.

## Run tests

```bash
pytest test_main.py -v
```

## Run with Docker

```bash
docker build -t task-tracker .
docker run -p 8000:8000 task-tracker
```

## What each piece demonstrates (and why it's on the resume)

| File | What it shows an interviewer |
|---|---|
| `auth.py` | You understand JWT auth, password hashing (bcrypt), and FastAPI's dependency injection for protected routes |
| `main.py` | Rate limiting (`slowapi`) on login/signup — a real security concern, not just decoration |
| `models.py` | A proper foreign-key relationship (`User` → `Task`), not a single flat table |
| `main.py` (`list_tasks`) | Data is scoped per-user — a very common interview question is "how do you stop user A from seeing user B's data?" |
| `test_main.py` | You write tests, including one that specifically checks the ownership/isolation logic above |
| `Dockerfile` | You know how to containerize an app for deployment |

## Resume bullet

> Built and deployed a task management REST API (FastAPI, SQLAlchemy, JWT auth, rate limiting)
> with per-user data isolation and Docker containerization; 4/4 test suite covering auth flows
> and ownership boundaries.

## Natural next steps to extend it further

- Swap SQLite for Postgres (`DATABASE_URL` env var already supports it)
- Add Redis caching on `GET /tasks` and measure the latency difference — gives you a real
  before/after number to quote
- Add a Celery worker for a background job (e.g. "email me a daily task summary") to show
  async/queue experience
- Deploy to Render or Railway and put the live URL + Swagger docs link on your resume
