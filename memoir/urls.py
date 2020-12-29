
from django.contrib import admin
from django.urls import path,include
from journal.views import index
from authapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/',index,name="index"),
    path('auth/',include('authapp.urls')),
    path('journal/',include('journal.urls')),
    path('notes/',include('notes.urls')),
    #path('api-auth/', include('rest_framework.urls'))
    
]
