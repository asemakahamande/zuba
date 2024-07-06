from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='Homepage'),
    path('Semester/', views.semester, name='semesterpage'),
    path('Semester/First/', views.semester1, name='firstsemesterpage'),
    path('Semester/Second/', views.semester2, name='secondsemesterpage'),
    path('Semester/Second/2023', views.semester2_2023, name='secondsemester2023'),
    path('Semester/First/2023', views.semester1_2023, name='firstsemester2023'),
    path('Admin/', views.admin, name='adminpage'),
    path('Contacts/', views.contacts, name='contactspage'),
    path('Login/', views.login, name='loginpage'),
    path('Help/', views.help, name='helppage'),
]
