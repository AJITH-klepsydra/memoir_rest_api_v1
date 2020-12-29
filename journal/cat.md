# Categorised list

Used to get list of journals/nots 

**URL** : `journal/category/<str:val>`<br>
<i>d-> diaries j-> journals</i><br>
**Method** : `GET`

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
    {
        "id": 15,
        "title": "ddsdd ",
        "published_date": "2020-12-29T13:35:32.785141Z",
        "description": "Corrected description1",
        "username": "test",
        "emotion": "Corrected emotion",
        "image": "default",
        "category": "d"
    },
    {
        "id": 17,
        "title": "ddsdd ",
        "published_date": "2020-12-29T13:38:14.304638Z",
        "description": "sd dsd",
        "username": "test",
        "emotion": "Corrected emotion",
        "image": "default",
        "category": "d"
    }
]
```

## Error Response

**Condition** : Incorrect value for val.

**Code** : `404 NOTFOUND`

**Content** :

```json

   "Journal does not exist"

```



