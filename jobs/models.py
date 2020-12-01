from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

class Company(models.Model):
    name = models.CharField()
    location = models.CharField()
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

class Specialty(models.Model):
    code = models.CharField()
    title = models.CharField()
    picture = models.URLField(default='https://place-hold.it/100x60')


