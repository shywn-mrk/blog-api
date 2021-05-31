# Blog API
A simple blog api for a blog :)

## Installation
Make sure you have Python >= 3.8 installed before following these steps.

1 - Clone the project:
`git clone https://github.com/shywn-mrk/shiny-winner.git`

2 - Create a virtual environment:
`python -m venv env`

3 - Activate the virtual environment:
- Windows:
`env/Scripts/activate`
- Mac/Linux:
`source env/bin/activate`

4 - Install the required packages:
`pip install -r requirements.txt`

5 - Creating migrations and migrate:
```
python manage.py makemigrations
python manage.py migrate
```
6 - Create a super user:
`python manage.py createsuperuser`

7 - Run the server:
`python manage.py runserver`

## Routes

All the routes are protected except for signup and login, this API uses token authentication.


### Admin Panel
you can access the django admin panel with this route (only super users can login!):<br/>
`GET /admin`

---

### Posts

#### All The Posts
`GET /api/posts`

#### Single Post
`/api/posts/:id`<br/>
Supported Methods: GET, POST, PUT, PATCH, DELETE

---

### Categories

#### All The Categories
`/api/categories`

#### Single Category
`/api/categories/:id`<br/>
Supported Methods: GET, POST, PUT, PATCH, DELETE

---

### Login
`POST /api/accounts/login`<br/>
Send username and password fields to this routes for authentication and getting your token back.

---

### SignUp
`POST /api/accounts/signup`<br/>
Send email and username and password fields to this routes to singup and getting a token.
