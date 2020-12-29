# Get current user info

Used to collect current user info for autherized users

**URL** : `/auth/users/me/`

**Method** : `GET PUT DELETE`

##GET

**Auth required** : YES


### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "email": "kk@kj.com",
    "id": 16,
    "username": "test"
}
```

### Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `401 UNAUTHORISED`

**Content** :

```json
{
    "detail": "Invalid token."
}
```




