# README for Backend Services

This project consists of a FastAPI server in Python and a REST API server in Java, along with a PostgreSQL database. The services are designed to communicate with each other and can be run together using Docker.

## Project Structure

```
backend-services
├── python-fastapi
│   ├── src
│   ├── requirements.txt
│   └── README.md
├── java-rest
│   ├── src
│   ├── pom.xml
│   └── README.md
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.x for the FastAPI application.
- Java 11 or higher for the Java REST application.

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd backend-services
   ```

2. Navigate to the `python-fastapi` directory and install the dependencies:
   ```
   cd python-fastapi
   pip install -r requirements.txt
   ```

3. Navigate to the `java-rest` directory and build the Java application:
   ```
   cd java-rest
   mvn clean install
   ```

4. Run the services using Docker Compose:
   ```
   docker-compose up
   ```

### Usage

- The FastAPI server will be accessible at `http://localhost:8000`.
- The Java REST server will be accessible at `http://localhost:8080`.

### Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

### License

This project is licensed under the MIT License.