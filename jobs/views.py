from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что-то пошло не так...Проверьте, что ввели ')


def custom_handler500(request):
    return HttpResponseServerError('Сервер прилег... Скоро починим')


def index(request):
    return render(request, 'index.html')

def vacancies(request):
    return render(request, 'vacancies.html')

def specialization(request,specialization_name):
    return render(request, 'specialization.html')

def company(request, company_id):
    return render(request, 'company.html',{})

def vacancy(request, vacancy_id):
    return render(request, 'vacancy.html',{})