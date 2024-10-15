# CT_ORM
Module 6, Lesson 3

```
python -m venv venv
python3 -m venv venv
venv\Scripts\activate
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Marshmallow
pip install mysql-connector-python
pip install mysqlclient
pip install pymysql
python.exe -m pip install --upgrade pip
```

For Mac:
```
python -m venv venv
python3 -m venv venv
source venv/bin/activate
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Marshmallow
pip install mysql-connector-python
pip install mysqlclient
pip install pymysql
python.exe -m pip install --upgrade pip
```
Create your database:
```
mysql -u root -p
CREATE DATABASE fitness_center_db;
```

Update this line within `app.py`: 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'

```
python app.py
pip freeze
```


Use a utility like postman to ping/reach ports:

http://127.0.0.1:5000/members (POST)

{
  "name": "John Doe",
  "email": "john@example.com"
}


Examine contents:
mysql -u root -p
USE fitness_center_db;
SELECT * FROM members;
