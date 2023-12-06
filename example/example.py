import os
from typing import Annotated
from hashlib import pbkdf2_hmac
from random import choice
from string import ascii_letters
from typing import Optional
from fastapi import FastAPI, APIRouter, Body
from pydantic import BaseModel, EmailStr, constr

from pprint import pprint


class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str]


class UserCreate(UserBase):
    password: str


class UserOutput(UserBase):
    hashed_password: str


class NewsBase(BaseModel):
    id: int
    title: str
    content: str


example_user_create = {
    'normal': {
        'value': {
            'id': 1,
            'email': 'example@email.com',
            'name': 'example',
            'password': 'example'
        }
    }
}

example_user_output = {
    'normal': {
        'value': {
            'id': 1,
            'email': 'example@email.com',
            'name': 'example',
            'password': 'b2867617492e26c338ab49f72afabc984d798b59755a27e312b953716ae964d7'
        }
    }
}

example_news_base = {
    'normal': {
        'value': {
            'id': 1,
            'title': 'example',
            'content': 'example'
        }
    }
}


def hash_password(password: str, salt: str = None):
    if not salt:
        salt = ''.join(choice(ascii_letters) for _ in range(12))
    return pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()


app = FastAPI(title='Тестовый проект', version='1.0')

router_user = APIRouter(prefix='/user', tags=['User'])
router_news = APIRouter(prefix='/news', tags=['News'])



@router_user.post('/', status_code=200, response_model=UserOutput)
async def create_user(user_info: Annotated[UserCreate, Body(examples=example_user_create)]):
    """
    Создание пользователя
    """
    return UserOutput(
        id = user_info.id,
        email=user_info.email,
        hashed_password=hash_password(user_info.password)
    )


@router_user.get('/', status_code=200, response_model=UserOutput)
async def get_user(user_id: int):
    """
    Получение пользователя
    """
    return UserOutput(
        id = user_id,
        email='example@mirea.ru',
        hashed_password=hash_password(password='example', salt='mirea')
    )


@router_news.post('/', status_code=200, response_model=NewsBase)
async def create_news(news_info: Annotated[NewsBase, Body(examples=example_news_base)]):
    """
    Создание новости
    """
    return news_info


@router_news.get('/', status_code=200, response_model=NewsBase)
async def get_news(news_id: int):
    """
    Получение новости
    """
    return NewsBase(
        id = news_id,
        title = 'Example Title',
        content= 'Example Content'
    )


app.include_router(router_user)
app.include_router(router_news)


if __name__ == '__main__':
    os.system('uvicorn main:app --reload')