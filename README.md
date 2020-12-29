# Memoir Rest API

Build with django, django restframework and djoser this api allow clients to post and retrieve journals.

'https://memoir-api-v1.herokuapp.com/'.

## Open Endpoints

Open endpoints require no Authentication.

* [Login](login.md) : `POST /auth/token/login/`
* [CheckServerTime](checkserver.md) : `GET /checkserver/`

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

### Current User related

Each endpoint manipulates or displays information related to the User whose
Token is provided with the request:

* [Show info](authapp/get.md) : `GET users/me/`
* [Update info](authapp/put.md) : `PUT users/me/`
### Account related

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.

* [Create Account](authapp/post.md) : `POST /auth/users/`

### Journal related

Endpoints for viewing and manipulating the journal that the Authenticated User
has permissions to access.

* [Create or Get All journals and diaries](journal/post.md) : `GET POST journal/`
* [Individual journal/diaries](journal/ind.md) : `GET PUT DELETE journal/<int:id>/`
* [Categorised list](journal/cat.md) : `GET journal/category/<str:val>/`

### Notes  related

Endpoints for viewing and manipulating the Notes that the Authenticated User
has permissions to access.

* [Create or Get All Notes](notes/post.md) : `GET POST notes/`
* [Individual note](notes/indnotes.md) : `GET PUT DELETE notes/<int:id>/`
