# Secure Log Analysis API

A secure, production-ready API for log analysis built with FastAPI.

## Features

- 🔒 Secure authentication and authorization
- 📊 Log analysis and processing
- 🚀 High-performance async API
- 📝 Comprehensive API documentation
- 🛡️ Security best practices

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Uvicorn** - ASGI server
- **bcrypt** - Password hashing
- **cryptography** - Cryptographic recipes and primitives
- **python-jose** - JWT token handling
- **passlib** - Password hashing library

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd secure-log-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Server

Start the development server with:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### Production Server

For production, use:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API docs (ReDoc)**: `http://localhost:8000/redoc`

## API Endpoints

### Health Check

- **GET** `/health`
  - Returns the health status of the API
  - Response: `{"ok": true}`

## Project Structure

```
secure-log-api/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore rules
```

## Development

### Adding Dependencies

To add a new dependency:
1. Install it: `pip install <package-name>`
2. Add it to `requirements.txt`: `pip freeze > requirements.txt`

### Code Style

Follow PEP 8 style guidelines for Python code.

## Security

This API implements security best practices including:
- Password hashing with bcrypt
- JWT token authentication
- Cryptographic primitives for sensitive operations

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

