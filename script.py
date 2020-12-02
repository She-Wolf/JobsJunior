import os
import django


os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

from jobs.models import Company, Specialty, Vacancy
from data import jobs, companies, specialties

if __name__ == '__main__':
    for company in companies:
        bd_company = Company.objects.create(
            name=company.get('title'),
            logo=company.get('logo'),
            employee_count=company.get('employee_count'),
            location=company.get('location'),
            description=company.get('description'),
        )
    print(bd_company)

    for specialty in specialties:
        bd_specialty = Specialty.objects.create(
            title=specialty.get('title'),
            code=specialty.get('code'),
        )
    print(bd_specialty)

    for vacancy in jobs:
        bd_vacancy = Vacancy.objects.create(
            title = vacancy.get('title'),
            specialty = Specialty.objects.get(code = vacancy.get('specialty')),
            company = vacancy.get('company'),
            skills =  vacancy.get('skills'),
            description = vacancy.get('description'),
            salary_min = vacancy.get('salary_from'),
            salary_max = vacancy.get('salary_to'),
            published_at = vacancy.get('posted'),
        )
    print(bd_vacancy)
