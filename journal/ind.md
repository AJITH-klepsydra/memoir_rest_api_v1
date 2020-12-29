# Accessing individual journal/notes entries

Used to get put and delete individual journal/notes

**URL** : `/journal/<int id>/`

**Method** : `GET PUT DELETE`

## GET
**Auth required** : YES



## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "id": 16,
    "title": "ddsdd ",
    "published_date": "2020-12-29T13:35:40.683994Z",
    "description": "sd dsd",
    "username": "test",
    "emotion": "Corrected emotion",
    "image": "default",
    "category": "d"
}
```

## Error Response

**Condition** : journal does not exist

**Code** : `404 NOT FOUND

**Content** :

```json
"Journal does not exist"
```



## PUT
**Auth required** : YES

**Data example**

```json
{
    "title":"[New title] ",
    "description":"[new description]",
    "emotion": "[new emotion]",
    "image": "[new image]",
    "category": "[category change]"
}
```



## Success Response

**Code** : `200 OK`

**Content example**
```json
{
    "id": 16,
    "title": "ddsdd ",
    "published_date": "2020-12-29T13:35:40.683994Z",
    "description": "sd dsd",
    "username": "test",
    "emotion": "Corrected emotion",
    "image": "default",
    "category": "j"
}
```
## DELETE
**Auth required** : YES

## Success Response

**Code** : `202 ACCEPTED`

**Content example**
```json
"Object deleted"
```
