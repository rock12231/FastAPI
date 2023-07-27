# FastAPI
CRUD API


#### Create virtual environment
```python -m venv venv```

#### Activate virtual environment
```source venv/bin/activate```

#### Install requirements
```pip install -r requirements.txt```

#### Run server
```uvicorn main:app --reload```

#### Create Database
``` CREATE DATABASE fastapi; ```

#### Use Database
``` USE fastapi; ```

#### Create Table
``` CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),email VARCHAR(100),age INT); ```   
