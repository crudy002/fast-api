# README for Python FastAPI Application

## Overview

This project contains a FastAPI application that serves as a backend service. It is designed to interact with a PostgreSQL database and can communicate with a Java REST API.

## Project Structure

```
backend-services
├── python-fastapi
│   ├── src
│   │   ├── main.py          # Entry point for the FastAPI application
│   │   ├── database.py      # Database connection and interactions
│   │   ├── models
│   │   │   └── __init__.py  # Data models for the application
│   │   └── routers
│   │       └── __init__.py  # API routes for the application
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # Documentation for the FastAPI application
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd backend-services/python-fastapi
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   You can start the FastAPI server using:
   ```bash
   uvicorn src.main:app --reload
   ```

4. **Access the API**:
   The FastAPI application will be available at `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Communication with Java REST API

This FastAPI application is designed to communicate with a Java REST API. Ensure that both services are running and properly configured to interact with each other.

## License

This project is licensed under the MIT License.