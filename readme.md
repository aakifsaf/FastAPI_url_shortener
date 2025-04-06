Project Overview

    This is a URL shortener API built with FastAPI and SQLAlchemy. It allows users to convert long URLs into unique 6-character short codes. When the short code is accessed, it redirects the user to the original long URL. Similar to services like Bitly or TinyURL. This project uses PostgreSQL as the database backend for persistent storage.

How it Works

1. Shortening a URL
- User sends a long URL using a POST request.
- A random 6-character alphanumeric short code is generated.
- It checks the database to ensure uniqueness.
- The long URL and short code are stored in the database.
- The short code is returned in the response.
2. Redirecting to Original URL
- When a user visits the short code URL, the backend fetches the original URL.
- If found, the user is redirected with an HTTP 307 status.
- If not found, a 404 error is returned.

How to Run the Project

    1. Create a Virtual Environment
        python -m venv venv
        source venv/bin/activate  (Windows: venv\Scripts\activate)
    2. Install Required Libraries
        pip install fastapi uvicorn sqlalchemy psycopg2-binary
    3.PostgreSQL Setup
        i.Create a PostgreSQL Database
            Use your PostgreSQL CLI or a GUI tool (like pgAdmin) to run the following commands:
                CREATE USER myuser WITH PASSWORD 'mypassword';
                CREATE DATABASE shortener_db OWNER myuser;
                GRANT ALL PRIVILEGES ON DATABASE shortener_db TO myuser;
        Replace myuser, mypassword, and shortener_db with your preferred username, password, and database name.
        ii.Update the Database URL
            In your database.py file, configure the database URL like so:
                SQLALCHEMY_DATABASE_URL="postgresql://myuser:mypassword@localhost/shortener_db"
            Ensure the values match the database credentials you created.
    4. Run the FastAPI Server
        uvicorn main:app --reload
        Visit http://127.0.0.1:8000/docs to test the API with Swagger UI.

API Endpoints

    1. POST /shorten/
    Description: Creates a short URL.
    Query Param: orgurl (the long URL)
    Example: /shorten/?orgurl=https://example.com/page
    Response: { 'shortcode': 'a1B2c3', 'message': 'successful' }
    2. GET /{shortcode}
    Description: Redirects to the original URL associated with the shortcode.
    Example: Visiting /a1B2c3 redirects to https://example.com/page

Summary

    This project uses FastAPI, PostgreSQL and SQLAlchemy to implement a basic but functional URL shortening service. Users can create short codes for long URLs and get redirected when accessing those codes. The backend ensures code uniqueness and handles redirection logic.