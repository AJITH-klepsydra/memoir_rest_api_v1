from django.urls import path,include
from journal import views


urlpatterns = [
	path('',views.journalPOST,name="journal_post"),
	path('<int:pk>/',views.journalGET,name="journal_get"),
	path('category/<str:val>',views.journalCAT,name="journal_cat"),
	#path('company/',views.companyApi)
	
]	
