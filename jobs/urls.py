from django.urls import path

from jobs import views

urlpatterns = [
    path('', views.index, name='home'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:vacancy_id>', views.vacancy, name='vacancy'),
    path('companies/<int:company_id>', views.company, name='company'),
    path('vacancies/cat/<str:speciality_name>', views.speciality, name='speciality'),

]
