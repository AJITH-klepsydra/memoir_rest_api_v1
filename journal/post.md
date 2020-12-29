# Create or get journal/notes

Used to create journal/note and to get all of them in publication date order

**URL** : `journal/`

**Method** : `POST GET`

## GET
**Auth required** : YES



## Success Response

**Code** : `200 OK`

**Content example**

```json
[
    {
        "id": 13,
        "title": "data ",
        "published_date": "2020-12-29T13:35:21.616411Z",
        "description": "Corrected description1",
        "username": "test",
        "emotion": "Corrected emotion",
        "image": "default",
        "category": "d"
    },
    {
        "id": 14,
        "title": "dd ",
        "published_date": "2020-12-29T13:35:26.773896Z",
        "description": "Corrected description1",
        "username": "test",
        "emotion": "Corrected emotion",
        "image": "default",
        "category": "d"
    },

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
    "title":"[]",
    "description":"[]",
    "emotion": "[emotion]",
    "image": "[url to an image]",
    "category": "[d for diary and j for journal]"
}
```



## Success Response

**Code** : `201 CREATED`

**Content example**

```json
"Object created"
```

