from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return f'id={self.pk},name= {self.name}, location = {self.location},' \
               f' description = {self.description} , employee_count = {self.employee_count}'

class Specialty(models.Model):
    code = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return f'id={self.pk},code= {self.code}, title = {self.title},' \
               f' picture = {self.picture}'

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return f'id={self.pk},specialty= {self.specialty},skills={self.skills},description={self.description},' \
               f'salary_min = {self.salary_min}, title = {self.title},' \
               f'salary_max = {self.salary_max}, published_at = {self.published_at}, company = {self.company}'