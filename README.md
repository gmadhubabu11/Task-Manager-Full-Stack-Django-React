# ✦ TaskFlow – Full-Stack Task Management System

A full-stack task management application inspired by Todoist, built with **React, Django REST Framework, MySQL, and JWT Authentication**.

TaskFlow helps users organize their daily activities by creating tasks, managing categories, setting priorities and due dates, tracking progress, and viewing dashboard statistics.


##  Project Overview

TaskFlow is a web-based task management system that allows users to manage their personal and professional tasks through an intuitive dashboard.

### Key Features

- User registration and login.
- JWT-based authentication.
- Automatic access token refresh.
- Protected frontend routes.
- Create, view, update, and delete tasks.
- Create, update, and delete categories.
- Assign categories to tasks.
- Task priorities: Low, Medium, High.
- Task statuses: To Do, In Progress, Done.
- Due date validation.
- Search tasks by keywords.
- Filter tasks by status, priority, category, and due date.
- Sort tasks by due date and priority.
- Dashboard with task statistics.
- Django Admin integration.
- REST API with Django REST Framework.

---

##  Technology Stack

### Frontend
- React
- Vite
- JavaScript
- React Router
- Axios
- CSS

### Backend
- Python
- Django
- Django REST Framework
- Simple JWT
- django-cors-headers
- django-filter
- Gunicorn
- WhiteNoise

### Database
- MySQL

### Development Tools
- Visual Studio Code
- MySQL Workbench
- Postman
- Git and GitHub

---

## Project Structure

```text
task-manager/
│
├── backend/
│   ├── accounts/
│   ├── tasks/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   └── migrations/
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── .env.example
│
├── postman/
│   └── Postman collection
│
├── screenshots/
│   └── Application screenshots
│
├── .gitignore
├── README.md
├── render.yaml
└── vercel.json
```

---

##  Prerequisites

Install the following before running the project:

- Python 3.10 or later
- Node.js and npm
- MySQL Server
- MySQL Workbench (optional)
- Git
- Visual Studio Code

---

#  Installation and Setup

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd task-manager
```

## 2. Backend Setup – Django

Open a terminal and navigate to the backend directory:

```bash
cd backend
```

### Step 1: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 2: Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file inside the `backend` directory using `.env.example` as a reference.

```powershell
Copy-Item .env.example .env
```

Update the values according to your local MySQL configuration.

Example:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
FRONTEND_URL=http://localhost:5173

DB_ENGINE=mysql
DB_NAME=task_manager
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

**Important:** Replace the example database credentials with your own. Never upload your actual `.env` file or secret key to GitHub.

### Step 5: Create the MySQL Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE task_manager;
```

Make sure your MySQL server is running and that the database details match your backend `.env` file.

### Step 6: Apply Database Migrations

```bash
python manage.py migrate
```

If you modify Django models, generate migrations:

```bash
python manage.py makemigrations
```

Then apply them:

```bash
python manage.py migrate
```

### Step 7: Create Django Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### Step 8: Run Backend Server

```bash
python manage.py runserver
```

Backend URL:

http://127.0.0.1:8000/

Django Admin:

http://127.0.0.1:8000/admin/

---

## 3. Frontend Setup – React

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

### Step 1: Install Dependencies

```bash
npm install
```

### Step 2: Configure Environment Variables

Create a `.env` file inside the frontend directory:

```powershell
Copy-Item .env.example .env
```

Configure the backend API URL:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

### Step 3: Start the Frontend

```bash
npm run dev
```

Frontend URL:

http://localhost:5173/

**Note:** Keep both the Django backend and React frontend servers running while using the application locally.

---

#  Authentication

TaskFlow uses JSON Web Token (JWT) authentication through Django REST Framework Simple JWT.

Authentication features include:

- User registration.
- User login.
- Access token generation.
- Refresh token generation.
- Automatic access token refresh.
- Protected API endpoints.
- Logout and token invalidation.

The default token configuration is:

| Token | Lifetime |
|---|---|
| Access Token | 30 minutes |
| Refresh Token | 1 day |

The frontend uses Axios interceptors to handle token refresh when an access token expires.

---

# API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api
```

## Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | User login |
| POST | `/auth/token/refresh/` | Refresh access token |
| GET | `/auth/me/` | Get current user details |
| POST | `/auth/change-password/` | Change account password |

## Category APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/categories/` | List categories |
| POST | `/categories/` | Create category |
| GET | `/categories/{id}/` | Retrieve category |
| PUT/PATCH | `/categories/{id}/` | Update category |
| DELETE | `/categories/{id}/` | Delete category |

## Task APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks/` | List tasks |
| POST | `/tasks/` | Create task |
| GET | `/tasks/{id}/` | Retrieve task |
| PUT/PATCH | `/tasks/{id}/` | Update task |
| DELETE | `/tasks/{id}/` | Delete task |
| GET | `/tasks/dashboard/` | Dashboard statistics |
| POST | `/tasks/{id}/toggle-complete/` | Toggle task completion |

**Note:** All protected endpoints require valid authentication. Use the JWT access token as a Bearer token in the Authorization header.

---

# 📋 Task Management

Users can organize tasks using the following properties:

| Property | Available Options |
|---|---|
| Priority | Low, Medium, High |
| Status | To Do, In Progress, Done |
| Category | Personal, Work, or custom categories |
| Due Date | Selected task deadline |

### Task Operations

- Create new tasks.
- Update existing tasks.
- Delete tasks with confirmation.
- Mark tasks as completed.
- Search tasks.
- Filter tasks.
- Sort tasks.
- Track overdue tasks.

---

#  Dashboard

The dashboard provides an overview of task progress.

It displays:

- Total tasks.
- To Do tasks.
- In Progress tasks.
- Completed tasks.
- Overdue tasks.
- Tasks due today.
- Completion percentage.
- Tasks grouped by category.

Dashboard statistics update according to task changes.

---

#  Testing with Postman

A Postman collection is included in the `postman/` directory.

To test the APIs:

1. Open Postman.
2. Import the provided Postman collection.
3. Start the Django backend.
4. Configure the API base URL.
5. Register a user and log in.
6. Use the returned JWT access token for protected endpoints.
7. Test authentication, categories, tasks, and dashboard APIs.

---

#  Application Screenshots

Application screenshots are available in the `screenshots/` directory.

The screenshots demonstrate:

- Registration and login pages.
- Dashboard.
- Task listing and task creation.
- Task editing.
- Category management.
- Past due date validation.
- Search, filters, and sorting.
- Task completion.
- Delete confirmation.
- Django Admin.

---

# Demo Workflow

The following workflow can be used to demonstrate the application:

1. Register a new user.
2. Log in and open the dashboard.
3. Refresh the page to verify login persistence.
4. Create categories.
5. Create tasks with different priorities and due dates.
6. Test past due date validation.
7. Search, filter, and sort tasks.
8. Mark a task as completed.
9. Edit an existing task.
10. Delete a task with confirmation.
11. Verify updated dashboard statistics.
12. Verify automatic JWT token refresh.
13. Log out.
14. Try accessing a protected route after logout.
15. Open Django Admin and inspect users, categories, and tasks.

---

# Deployment

The project is intended to be deployed using:

| Component | Platform |
|---|---|
| Frontend | Vercel |
| Backend | Render |
| Database | MySQL |

For production deployment:

- Configure production environment variables.
- Use a production MySQL database.
- Set the correct allowed hosts.
- Configure CORS for the deployed frontend domain.
- Run database migrations.
- Build and deploy the React frontend.
- Configure the frontend API URL to point to the deployed backend.

Deployment links:

- GitHub Repository: To be added
- Frontend (Vercel): To be added
- Backend (Render): To be added

---

#  Security Notes

- Environment variables are used for sensitive configuration.
- Actual `.env` files must not be committed.
- JWT authentication protects user-specific API access.
- CORS is configured for frontend communication.
- Passwords are handled through Django authentication.
- Users should not share their login credentials or tokens.

---

#  Author

**madhu babu**

Full-Stack Developer | Python Developer

GitHub: https://github.com/madhu babu

---

##  License

This project was developed for educational and learning purposes as part of a full-stack development assignment