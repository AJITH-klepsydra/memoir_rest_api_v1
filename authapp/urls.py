from django.urls import path,include
from authapp import views
from authapp import models

urlpatterns = [
	path('',include('djoser.urls')),
	path('',include('djoser.urls.authtoken')),
	#path('company/',views.companyApi)
	
]	