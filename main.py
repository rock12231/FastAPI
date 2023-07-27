# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

mysql_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "fastapi",
    "port": "3307",
}
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()


class User(BaseModel):
    name: str
    email: str
    age: int


def create_users_table():
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        age INT
    )
    """
    cursor.execute(query)
    conn.commit()


@app.post("/users/", response_model=User)
async def create_user(user: User):
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    values = (user.name, user.email, user.age)
    cursor.execute(query, values)
    conn.commit()
    return user


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    query = "SELECT id, name, email, age FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "age": user[3],
    }


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s"
    values = (user.name, user.email, user.age, user_id)
    cursor.execute(query, values)
    conn.commit()
    return {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    return {"message": "User deleted successfully"}

create_users_table()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
