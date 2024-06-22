                                                           User Management System API with Django and DRF
This repository contains a User Management System API built using Django and Django Rest Framework (DRF). The API provides endpoints for managing user data including creation, retrieval, update, and deletion operations.

*********Features
API Overview: Displays available endpoints and their descriptions.
User List: Retrieves a list of all users.
Retrieve User by Name: Retrieves user details by username.
Retrieve User by ID: Retrieves user details by user ID.
Create User: Creates a new user with username, first name, last name, email, and password.
Update User by Name: Updates user details identified by username.
Update User by ID: Updates user details identified by user ID.
Delete User by Name: Deletes a user identified by username.
Delete User by ID: Deletes a user identified by user ID.
Installation and Setup
To run the User Management System API locally, follow these steps:

**********Clone the repository:

git clone <repository-url>
cd <repository-directory>

*****Install dependencies:
pip install -r requirements.txt


****Apply database migrations:
python manage.py migrate


***Run the development server:
python manage.py runserver

****Access the API:
Open your web browser or use an API client like Postman and access the endpoints:

http://127.0.0.1:8000/user-list/ (GET) - Retrieve list of users
http://127.0.0.1:8000/user-detail/?username=<username> (GET) - Retrieve user by username
http://127.0.0.1:8000/user-detail/<pk>/ (GET) - Retrieve user by ID
http://127.0.0.1:8000/user-create/ (POST) - Create a new user
http://127.0.0.1:8000/user-update/?old_name=<old_name> (PUT) - Update user by username
http://127.0.0.1:8000/user-update/<pk>/ (PUT) - Update user by ID
http://127.0.0.1:8000/user-delete-by-name/?username=<username> (DELETE) - Delete user by username
http://127.0.0.1:8000/user-delete/<pk>/ (DELETE) - Delete user by ID
