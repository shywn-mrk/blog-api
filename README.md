# Blog API
A simple blog api for a blog :)

## Running The Project

### Clone The Project
`git clone https://github.com/shywn-mrk/blog-api.git`

### Create The Enviroment
In the root of the project run:
`python -m venv env`

### Activating The Enviroment
Activate the enviroment using:
`source env/Scripts/activate`

### Install The Packages
Install the required packages using:
`pip install -r requirements.txt`

### Migrate The Models
Migrate the models to the database using:
`python manage.py migrate`

### Create a Super User
Create a super user using:
`python manage.py createsuperuser`

### Run The Server
Run the server using:
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