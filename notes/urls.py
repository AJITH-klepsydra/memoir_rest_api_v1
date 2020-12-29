
from django.urls import path,include

from notes import views
urlpatterns = [
    path('',views.NotesPOST,name="journal_post"),
	path('<int:pk>/',views.NotesGET,name="journal_get"),
    #path('api-auth/', include('rest_framework.urls'))
    
]
