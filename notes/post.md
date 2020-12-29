# Create or get journal/notes

Used to create notes and to get all of them in publication date order

**URL** : `notes/`

**Method** : `POST GET`

## GET
**Auth required** : YES



## Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 2,
        "title": "sas",
        "published_date": "2020-12-29T15:06:07.705659Z",
        "description": "aijs",
        "username": "test",
        "end_date": "2020-12-26T01:14:25Z"
    },
    {
        "id": 3,
        "title": "hhh",
        "published_date": "2020-12-29T15:06:14.019903Z",
        "description": "aijs",
        "username": "test",
        "end_date": "2020-12-26T01:14:25Z"
    }
]
```

## Error Response

**Condition** : Incorrect authorisation token.

**Code** : `401 UNAUTHORISED`

**Content** :

```json
{
    "detail": "Authentication credentials were not provided."
}
```



## POST
**Auth required** : YES

**Data example**

```json
{

    "title": "hhh",
    "description": "aijs",
    "end_date":"2020-12-26 01:14:25"

}
```



## Success Response

**Code** : `201 CREATED`

**Content example**

```json
"Object created"
```

