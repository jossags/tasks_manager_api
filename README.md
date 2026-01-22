# Task Management API
A small REST API built with *Django* and *Django REST Framework* for personal task management. This project includes authentication, owner permissions, and filtering functionalities.

# Key Features
- Authentication: Signup and Login using Tokens.
- Privacy: Each user can only manage their own tasks.
- CRUD: Create, Read, Update, and Delete tasks.
- Filters: 
  - Sort by priority (`asc`/`desc`).
  - Search by task title.
- Date Control: Automatic validation to ensure the due date is not in the past.

# Installation and Setup
1. Clone the repository:
   git clone https://github.com/jossags/tasks_manager_api.git

2. Dependencies
    pip install -r requirements.txt

3. Migrations
    python manage.py migrate

4. Start Server
    python manage.py runserver

# Endpoints
Method      Endpoint           Description
POST        /api/signup/       Create a new account.
POST        /api/login/        Obtain access Token.
POST        /api/logout/       Invalidate current Token.

# Tasks (Token Required)
Method      Endpoint            Description
GET         /api/tasks/         List all my tasks.
POST        /api/tasks/         Create a new task.
GET         /api/tasks/<id>/    View task details.
PUT         /api/tasks/<id>/    Update a task.
DELETE      /api/tasks/<id>/    Delete a task.

# Security (SECRET_KEY)
Note: For practical purposes of this challenge, the SECRET_KEY is kept in the code. D:

