# README for Java REST Application

This project contains a Java REST application built using Spring Boot. It is designed to work alongside a FastAPI server and a PostgreSQL database.

## Project Structure

- `src/main/java/com/example/Application.java`: Entry point for the Spring Boot application.
- `src/main/java/com/example/controller/ApiController.java`: Contains the REST API endpoints.
- `src/main/resources/application.properties`: Configuration settings for the application.
- `pom.xml`: Maven configuration file for managing dependencies.

## Setup Instructions

1. **Prerequisites**: Ensure you have Java JDK and Maven installed on your machine.
2. **Clone the Repository**: Clone this repository to your local machine.
3. **Navigate to the Project Directory**: Open a terminal and navigate to the `java-rest` directory.
4. **Build the Project**: Run the following command to build the project:
   ```
   mvn clean install
   ```
5. **Run the Application**: Start the application using the following command:
   ```
   mvn spring-boot:run
   ```

## Usage

Once the application is running, you can access the REST API endpoints defined in `ApiController.java`. Make sure the FastAPI server and PostgreSQL database are also running for full functionality.

## Additional Information

Refer to the main project `README.md` for instructions on setting up and running the entire backend services, including the FastAPI server and PostgreSQL database.