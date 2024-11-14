from fastapi import FastAPI

app = FastAPI()


@app.get('/user/admin')
async def welcome():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def welcome(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def welcome(username: str, age: int):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}
