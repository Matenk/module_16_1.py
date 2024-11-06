from fastapi import FastAPI
from pyexpat.errors import messages

app = FastAPI()




@app.get('/user/admin')
async def welcome_admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def welcome_user(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def user_info(username: str, age: int):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}.'}


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}