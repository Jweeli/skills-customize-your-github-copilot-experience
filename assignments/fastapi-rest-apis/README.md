# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern REST APIs using FastAPI framework by creating a todo application API. You'll understand HTTP methods, request/response handling, and how to structure API endpoints for real-world applications.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description
Set up your FastAPI development environment and create the basic project structure. You'll learn how to install dependencies, create a FastAPI application, and run the development server.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a main application file that initializes FastAPI
- Run the development server on localhost:8000
- Test the root endpoint returns a welcome message


### 🛠️ Create Todo Model and GET Endpoints

#### Description
Define a todo data model and implement GET endpoints to retrieve todos. You'll learn about request validation and data serialization in FastAPI.

#### Requirements
Completed program should:

- Define a Todo model with fields: id, title, description, completed (boolean)
- Implement a GET endpoint that returns all todos
- Implement a GET endpoint that retrieves a specific todo by id
- Include proper error handling for non-existent todo items
- Return appropriate HTTP status codes (200, 404)


### 🛠️ Implement POST and PUT Endpoints

#### Description
Add endpoints to create new todos and update existing ones. You'll practice request body validation and data mutation operations.

#### Requirements
Completed program should:

- Implement a POST endpoint to create new todos with auto-generated id
- Implement a PUT endpoint to update a specific todo by id
- Validate required fields in request bodies
- Return the created/updated todo with appropriate HTTP status codes (201, 200, 404)


### 🛠️ Add DELETE Endpoint and Error Handling

#### Description
Complete the CRUD operations by implementing the DELETE endpoint with comprehensive error handling.

#### Requirements
Completed program should:

- Implement a DELETE endpoint to remove a todo by id
- Return appropriate status codes (204 for success, 404 for not found)
- Include meaningful error messages for all edge cases
- Test all endpoints using the interactive API documentation at /docs
