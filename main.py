from fastapi import FastAPI

app = FastAPI()


@app.get('/user/admin')
async def welcom():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def welcom(user_id: int):
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def welcom(username: str, age: int):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def welcom():
    return {'message': 'Главная страница'}