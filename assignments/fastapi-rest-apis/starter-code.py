from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI()

# Define the Todo model
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for todos (for this assignment)
todos_db = []
next_id = 1

# Root endpoint - Welcome message
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Todo API"}

# TODO: Implement GET /todos endpoint to return all todos

# TODO: Implement GET /todos/{todo_id} endpoint to retrieve a specific todo

# TODO: Implement POST /todos endpoint to create a new todo

# TODO: Implement PUT /todos/{todo_id} endpoint to update a todo

# TODO: Implement DELETE /todos/{todo_id} endpoint to delete a todo

# Instructions:
# 1. Run the server with: uvicorn starter-code:app --reload
# 2. Access the interactive API docs at: http://localhost:8000/docs
# 3. Implement the TODO endpoints above
# 4. Test all endpoints using the built-in documentation
