
# 📱 FastAPI Social Media API

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-336791?logo=postgresql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?logo=sqlalchemy&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange) ![JWT](https://img.shields.io/badge/Auth-JWT-yellow?logo=jsonwebtokens&logoColor=black) ![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-green?logo=gunicorn&logoColor=white) ![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-ff69b4?logo=python&logoColor=white) ![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)

A **production-ready social media backend API** built with FastAPI.  
It allows users to create posts, interact with content, and manage accounts securely using JWT authentication.

----------
## 📌 Problem Statement

Modern applications require scalable backend systems to manage user-generated content, authentication, and interactions.  
This project provides a RESTful API to handle posts, users, and engagement efficiently.

----------
## 🚀 Features

-   🔐 **JWT Authentication** (Login & Secure Access)
    
-   👤 **User Management** (Register & View Users)
    
-   📝 **CRUD Operations on Posts**
    
-   👍 **Voting System on Posts**
    
-   🗄️ **PostgreSQL Database Integration**
    
-   🔄 **Database Migrations using Alembic**
    
-   ⚡ **Production Deployment (Gunicorn + Uvicorn)**
    

----------
## 🛠 Tech Stack

-   **Backend**: Python, FastAPI
    
-   **Database**: PostgreSQL
    
-   **ORM**: SQLAlchemy
    
-   **Authentication**: JWT
    
-   **Migrations**: Alembic
    
-   **Deployment**: Render (Gunicorn + Uvicorn)
    

----------
## 📁 Project Structure

```bash
app/
 ├── main.py
 ├── models/
 ├── schemas/
 ├── routers/
 ├── database/
 ├── oauth2/
 ├── config/

```

----------
## 🔄 How It Works

1.  User registers and logs in to receive a JWT token
    
2.  Authenticated users can create, update, and delete posts
    
3.  Users can view all posts and interact via voting
    
4.  Database stores users, posts, and votes with relationships
    

----------
## 📌 API Endpoints

### 🔑 Authentication

-   **POST** `/login` → Authenticate user & get JWT token
    

----------
### 👤 Users

-   **POST** `/users/` → Register a new user
    
-   **GET** `/users/{id}` → Get user details
    

----------
### 📝 Posts

-   **GET** `/posts/` → Get all posts
    
-   **GET** `/posts/{id}` → Get a single post
    
-   **POST** `/posts/` → Create post _(Auth required)_
    
-   **PUT** `/posts/{id}` → Update post _(Auth required)_
    
-   **DELETE** `/posts/{id}` → Delete post _(Auth required)_
    

----------
### 👍 Votes

-   **POST** `/votes/` → Vote on a post _(Auth required)_
    

----------
## ⚙️ Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/janakiramayya04/fastapi_socialmedia.git
cd fastapi_socialmedia

```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure environment variables

Create `.env` file:

```bash
DATABASE_URL="your_postgresql_database_url"
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"

```

### 5. Run database migrations

```bash
alembic upgrade head

```

### 6. Run the application

```bash
uvicorn app.main:app --reload

```

👉 Access API docs:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

----------
## 🌍 Deployment

This application is deployed using **Render** with:

-   **Gunicorn** as process manager
    
-   **Uvicorn workers** for ASGI handling
    
-   `render.yaml` for deployment configuration
    

----------
## 🚀 Future Improvements

-   Follow/Unfollow users
    
-   Comments system
    
-   Notifications
    
-   Rate limiting
    
-   API pagination & caching
    

----------
## 📜 License

This project is licensed under the MIT License.
