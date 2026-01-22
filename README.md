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

# Technical Decisions & Tools
1. **Django REST Framework:** Used primarily because the challenge required it haha, but it was especially useful as it handled response codes and data conversion to JSON.
2. **Token Authentication:** It literally saved my life; it created the ENTIRE authentication system. I used it because it is very comprehensive.
3. **Django ORM:** Mainly for productivity, as the code is faster to write; it also comes with built-in security and, from what I understand, even though I'm using SQLite, if we wanted to switch to MySQL later, the ORM would do that job for me :D
4. **Git & GitHub:** Honestly, it's the first time I've done commits and such, so I used the tools listed in parentheses () in the challenge; it was more of a requirement than a personal reference for me haha.
5. **Thunder Client:** I used it because it's very simple; there I could test the endpoints, headers, and JSON validation, as well as the filters. It was very helpful and its interface is very user-friendly.
