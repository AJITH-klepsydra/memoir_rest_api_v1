# CREATE USER

Used to create a new user

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : YES



**Data constraints**

```json
{
    "username": "[username]",
    "password": "[password]",
    "re_password": "[confirm password]",
    "email":"[valid email id]"
}
```

## Success Response

**Code** : `201 CREATED`

**Content example**

```json
{
    "email": "kk@kj.com",
    "username": "test22",
    "id": 18
}
```

## Error Response

**Condition** :user already exist.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "username": [
        "A user with that username already exists."
    ]
}
```
