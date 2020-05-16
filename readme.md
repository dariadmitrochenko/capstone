# Udacity FSND Capstone Project
*by Daria Dmitrochenko*
## Motivation
This is the final Project of the Udacity's Fullstack Nanodegree. It's the Casting Agency API, that allows users to view, add and delete movies and actors, according to their authorized roles.

The project
demonstrates the ability to build the backend for an application with **CRUD** functionality (Create, Update, Delete) and **RESTful API** principles using **Python** and **JSON**,
interact with databases using **SQL**, test with **Postman** tool
(role-based authentification and authorization with **Auth0**), and deploy the application
using **Heroku**. All of the above are the skills gained through Udacity's FSND Nanodegree.


Follow this [link](https://fsnd-capstone-casting-agency.herokuapp.com/) to view the app live on Heroku
### Key Dependencies
#### Python 3.7
First and foremost, you'll need **Python 3.7**. [Click here](https://realpython.com/installing-python/) for a very detailed instruction on installation for Windows and MacOS.
#### Flask
[Click here](http://flask.pocoo.org/docs/1.0/installation/#install-flask) and follow instructions to install Flask, which is a very convenient framework to handle requests.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```
You'll also need **Flask-CORS** which is a simple extension to Flask allowing you to support cross origin resource sharing (CORS) using a simple decorator
 ```
 $ pip3 install flask-cors
 ```

 #### SQLAlchemy
 SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
 Click [here](https://www.pythoncentral.io/how-to-install-sqlalchemy/) to install on Windows, MacOS or Linux


 #### virtualenv
 To avoid interfering with your machine's set up, use Virtual Environment for further dependencies installations. Instructions on how to start a virtualenv below.
### Running the server
To start and run the local development server,

1. Fork this repository and save it to your local machine
2. Initialize and activate a virtualenv. From your Terminal run:
```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install the dependencies:
```
$ pip install -r requirements.txt
  ```

4. Run
```
$ python app.py
```
Alternatively, you can run the server with *flask run* command like so:
```
$ export FLASK_APP=app
$ flask run
```
5. Go to http://localhost:8080/

### APIs and RBAC
The server has several API endpoints. Each of them can be reached through *Role Based Authentification* with a JWT token. The roles are: Casting Assistant, Director, Producer.

1. GET (view)

`/actors` to get:actors

`/movies` to get:movies

*Available to all roles*

2. POST (create)

`/movie/create` to post:movie

`/actors/create` to post:actor

3. PATCH (update)

`/actors/<int:actor_id>` to patch:actor

`/movies/<int:movie_id>` to patch:movie

4. DELETE

`/movies/delete/<int:movie_id>` to delete:movie

`/actors/delete/<int:actor_id>` to delete:actor

#### Roles
*Producer* can access any endpoint

*Director* is not allowed to create, patch or delete movies

*Assistant* can only view actors and movies

#### Tokens
To generate a token:
[Click here](https://udacityfullstack.auth0.com/authorize?audience=coffeeshop&response_type=token&client_id=RuwZLTCCH3AGAekA3hWcBAJfHpAeydYc&redirect_uri=http://localhost:8080) and login with Auth0

To logout: [Click here](https://udacityfullstack.auth0.com/logout)

For testing purposes logins and passwords are generic and listed below. However, in real world this data is sensitive and thus should be protected.

**Producer:**

login: producer@email.com

password: producer

**Director:**

login: director@email.com

password: director

**Assistant:**

login: assistant@email.com

password: assistant




## Testing with Postman
1. Download Postman [here](https://www.postman.com/downloads/application) and follow the installation instructions
2. Open Postman and click **Import** in the far left corner
3. Import *Capstone FSND test collection* from the project folder. The tokens will be valid for 20 hours.
4. Run the collection. The tests are configured to prove the ability to perform
different CRUD operations according to a certain role and its permissions (Producer
  can perform all operations, Director can do anything but post or delete a movie, assistant can only view actors and movies)
