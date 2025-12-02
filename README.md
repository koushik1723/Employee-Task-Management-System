📌 Employee Task Management System

A full-stack web application that allows users to manage Employees and Tasks, featuring authentication, CRUD operations, and database integration.

This project is built as part of:

 Backend Development (API )
using FastAPI and a connected frontend.




🧰 Tech Stack Used

  BACKEND
  
| Technology            | Purpose                           |
| --------------------- | --------------------------------- |
| **FastAPI**           | Backend API framework             |
| **Python**            | Programming language              |
| **SQLAlchemy ORM**    | Database ORM layer                |
| **Pydantic**          | Data validation and schemas       |
| **SQLite**            | Local database storage            |
| **JWT (python-jose)** | Authentication & token generation |
| **Uvicorn**           | ASGI server for FastAPI           |
| **Passlib (bcrypt)**  | Password hashing                  |

FRONTEND

| Technology                 | Purpose                                 |
| -------------------------- | --------------------------------------- |
| **HTML5**                  | Structure of the UI                     |
| **CSS3**                   | Styling and layout                      |
| **JavaScript (Fetch API)** | API integration & dynamic functionality |






🚀 Setup Steps

1. Backend Setup (FastAPI)

| Step                                   | Command                             |
| -------------------------------------- | ----------------------------------- |
| Create virtual environment             | `python -m venv venv`               |
| Activate virtual environment (Windows) | `venv\Scripts\activate`             |
| Install dependencies                   | `pip install -r requirements.txt`   |
| Start backend server                   | `uvicorn backend.main:app --reload` |
| Default backend URL                    | `http://127.0.0.1:8000`             


 
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/8acd55c4-c92c-407c-bff6-1c4082c10271" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/72683249-eee8-4d06-a7f4-33a0f8cf9259" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/84f6f6a4-f1eb-424a-b83b-f2b21f772cfa" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/02c5f569-c37a-4ac6-ac85-13854fb633db" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/0ebe2ec8-e57c-42a5-966c-14700fd1324b" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/e636e7cb-955b-42e7-8319-deeb0e3e0b60" />

 FASTAPI SWAGGER UI
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/961e04e8-0dce-4655-822f-c71e9166329c" />
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/077035ce-446c-41fb-b86f-6d87b1ef9c7d" />

📝 Assumptions

-> Every logged-in user is allowed to manage all employees/tasks.
-> SQLite is used for simplicity; can be upgraded to PostgreSQL.
-> Frontend is lightweight and uses only vanilla JavaScript.
-> All task/employee relations follow a 1-to-many structure.


BONUS FEATURES IMPLEMENTED

✔ Full JWT Authentication (Login + Protected Routes)
✔ Complete CRUD for Employees & Tasks
✔ Extra API Endpoints:
  > Get all tasks of an employee
  > Get employee assigned to a task
  > Get only the employee name
  > Get only task titles
THIS PROJECT IS PRIMARILY FOCUSED ON BACKEND DEVELOPMENT AND CLOUD DEPLOYMENT. THE FRONTEND PART IS INTENTIONALLY MINIMAL AND NOT THE MAIN SCOPE OF THE PROJECT.









