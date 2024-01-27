# Task Manager - Flask

### Design of a simple task manager to exercise CRUD concepts on a SQLite3 database using Flask and SQLAlchemy.
#### Technologies used: Python, Flask, HTML and CSS (Bootstrap)



![App Screenshot](https://img001.prntscr.com/file/img001/eGfL-7GBT1auxzOIVNxkWw.png)



## Install

1. Create your virtual environment.
2. Install the requirements contained in requirements.txt with the command  ```pip install -r requirements.txt.```

3. In the project directory, use ```flask --app app.py db upgrade``` to create the SQLITE3 database file according to the established settings and also the migrations contained in the migrations folder.
4. Run the file run.py

## How it works

#### Execution takes place via flask, where we define a flask app in the app.py file, and there we make the app settings, for the SqlAlchemy ORM and for migration, there we also inform the app, the routes contained in the controllers module in the routes file and also the models, to carry out the migration.

#### How the application works is through a CRUD performed on the "Tasks" table that we created through the "Task" model that we created and migrated to a local SQLite3 database. When we access the "index" route, all the records in the Tasks table are loaded and there we can filter by the Status field which ones have been completed and which ones have not. We also have the option of inserting data into this table, where a new page is opened in a route where we have a form that we fill in and this data creates a new record in the table, and we also have the option of deleting/changing these records. where it happens that through the ID, we select a record and modify it. This project was done using bootstrap to style the html templates.

### Python Version 3.11x