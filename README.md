# GitTracker API

GitTracker is a FastAPI-based service that provides an easy way to track GitHub user contribution stats and activity.

## Overview

GitTracker API allows you to retrieve various information about GitHub users, including their:

- Basic profile information
- Top repositories
- Language usage statistics
- Recent activity

## Project Structure

```
app/
├── api/
│   ├── endpoints/
│   │   ├── __init__.py
│   │   └── github.py
│   ├── __init__.py
│   └── routes.py
├── schemas/
│   ├── __init__.py
│   └── github_schema.py
├── services/
│   ├── __init__.py
│   └── github_service.py
├── tests/
│   ├── __init__.py
│   └── test_github.py
├── __init__.py
└── main.py
```

## Features

### 1. User Summary
Retrieve basic information about a GitHub user including name, follower count, repository count, and profile links.

### 2. User Repositories
Get a user's top repositories sorted by various metrics (stars, forks, etc.).

### 3. Language Usage
See what programming languages a user works with most frequently, presented as percentages.

### 4. User Activity
Track a user's recent public activity on GitHub.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/{username}/summary` | GET | Get basic user information |
| `/api/users/{username}/repos` | GET | Get top repositories with sorting and limit options |
| `/api/users/{username}/languages` | GET | Get language usage statistics |
| `/api/users/{username}/activity` | GET | Get recent public activity |

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Service

```bash
fastapi run
```

## API Documentation

Once the service is running, you can access the auto-generated Swagger documentation at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Testing

Run tests with pytest:

```bash
pytest
```
