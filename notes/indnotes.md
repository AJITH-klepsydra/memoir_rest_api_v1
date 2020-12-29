# Accessing Notes

Used to get put and delete individual journal/notes

**URL** : `/notes/<int id>/`

**Method** : `GET PUT DELETE`

## GET
**Auth required** : YES



## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "id": 2,
    "title": "sas",
    "published_date": "2020-12-29T15:06:07.705659Z",
    "description": "aijs",
    "username": "test",
    "end_date": "2020-12-26T01:14:25Z"
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
    "id": 2,
    "title": "sas",
    "description": "aijs",
    "end_date": "2020-12-26T01:14:25Z"
}
```



## Success Response

**Code** : `200 OK`

**Content example**
```json
{
    "id": 2,
    "title": "sas",
    "published_date": "2020-12-29T15:06:07.705659Z",
    "description": "aijs",
    "username": "test",
    "end_date": "2020-12-26T01:14:25Z"
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
