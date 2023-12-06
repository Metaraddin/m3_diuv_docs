# Тестовый проект 1.0

openapi version 3.0.2

## GET /user/

Get User

Получение пользователя
### Parameters

| Name | Type | Required |
|-|-|-|
| user_id | integer | True |  |

### Responses

#### 200

Successful Response

[UserOutput](#useroutput)
#### 422

Validation Error

[HTTPValidationError](#httpvalidationerror)

## POST /user/

Create User

Создание пользователя
### Request Body

[UserCreate](#usercreate)

#### Examples

```json
{
  "id": 1,
  "email": "example@email.com",
  "name": "example",
  "password": "example"
}
```



### Responses

#### 200

Successful Response

[UserOutput](#useroutput)
#### 422

Validation Error

[HTTPValidationError](#httpvalidationerror)

## GET /news/

Get News

Получение новости
### Parameters

| Name | Type | Required |
|-|-|-|
| news_id | integer | True |  |

### Responses

#### 200

Successful Response

[NewsBase](#newsbase)
#### 422

Validation Error

[HTTPValidationError](#httpvalidationerror)

## POST /news/

Create News

Создание новости
### Request Body

[NewsBase](#newsbase)

#### Examples

```json
{
  "id": 1,
  "title": "example",
  "content": "example"
}
```



### Responses

#### 200

Successful Response

[NewsBase](#newsbase)
#### 422

Validation Error

[HTTPValidationError](#httpvalidationerror)
## Components

### HTTPValidationError

| Field | Type |
|-|-|
| detail | array |

### NewsBase

| Field | Type |
|-|-|
| id | integer |
| title | string |
| content | string |

### UserCreate

| Field | Type |
|-|-|
| id | integer |
| email | string |
| name | string |
| password | string |

### UserOutput

| Field | Type |
|-|-|
| id | integer |
| email | string |
| name | string |
| hashed_password | string |

### ValidationError

| Field | Type |
|-|-|
| loc | array |
| msg | string |
| type | string |