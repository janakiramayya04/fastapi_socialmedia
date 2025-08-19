
# FastAPI Social Media ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-336791?logo=postgresql&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?logo=sqlalchemy&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange) ![JWT](https://img.shields.io/badge/Auth-JWT-yellow?logo=jsonwebtokens&logoColor=black) ![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-green?logo=gunicorn&logoColor=white) ![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-ff69b4?logo=python&logoColor=white) ![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)

A social media application built with **FastAPI**, providing a RESTful API for users to create posts, vote on posts, and manage their accounts.

---
## 🚀 Features
- **User Authentication**: Secure user registration and login using JWT tokens.  
- **CRUD Posts**: Users can create, view, update, and delete their own posts.  
- **Voting System**: Users can vote on posts.  
- **Database Migrations**: Alembic is used for schema migrations.  
- **ORM**: SQLAlchemy is used to interact with the PostgreSQL database.  

---

## 🛠️ Technologies Used
- **Backend**: Python, FastAPI  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Authentication**: JWT (JSON Web Tokens)  
- **Dependency Management**: pip  
- **Database Migrations**: Alembic  
- **Deployment**: Gunicorn, Uvicorn, Render  

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/janakiramayya04/fastapi_socialmedia.git
cd fastapi_socialmedia
```
### 2. Create a virtual environment and activate it 
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
 Create a `.env` file in the root directory and add:
 ```bash
 DATABASE_URL="your_postgresql_database_url"
SECRET_KEY="your_secret_key"
ALGORITHM="your_jwt_algorithm" 
```
### 5. Run database migrations
```bash 
alembic upgrade head
```
### ▶️ Usage
Run the application with Uvicorn:
```bash
uvicorn app.main:app --reload
```
The application will be available at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📌 API Endpoints

### 🔑 Authentication

-   **POST** `/login` → Authenticate a user and get a JWT token
    

### 👤 Users

-   **POST** `/users/` → Create a new user
    
-   **GET** `/users/{id}` → Get a user by ID
    

### 📝 Posts

-   **GET** `/posts/` → Get all posts
    
-   **GET** `/posts/{id}` → Get a single post by ID
    
-   **POST** `/posts/` → Create a new post _(requires authentication)_
    
-   **PUT** `/posts/{id}` → Update a post _(requires authentication)_
    
-   **DELETE** `/posts/{id}` → Delete a post _(requires authentication)_
    

### 👍 Votes

-   **POST** `/votes/` → Cast a vote on a post _(requires authentication)_
    

----------

## 🌍 Deployment

This application is configured for deployment on **Render**.  
The `render.yaml` file defines the service configuration.  
The application is served using **Gunicorn** with **Uvicorn workers**.
