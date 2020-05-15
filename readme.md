# Udacity FSND Capstone Project
*by Daria Dmitrochenko*
## Overview
This is the final Project of the Udacity's Fullstack Nanodegree. The project
demonstrates the ability to build the backend for an application with **CRUD** functionality (Create, Update, Delete) and **RESTful API** principles using **Python** and **JSON**,
interact with databases using **SQL**, test with **Postman** tool
(role-based authentification and authorization with **Auth0**), and deploy the application
using **Heroku**.
## Getting Started
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
$python app.py
```

## Testing with Postman
1. Download Postman [here](https://www.postman.com/downloads/application) and follow the installation instructions
2. Open Postman and click **Import** in the far left corner
3. Import *Capstone FSND test collection* from the project folder. The tokens will be valid for 20 hours.
4. Run the collection. The tests are configured to prove the ability to perform
different CRUD operations according to a certain role and its permissions (Producer
  can perform all operations, Director can do anything but post or delete a movie, assistant can only view actors and movies)
