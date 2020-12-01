import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

from jobs.models import Company,Specialty,Vacancy

if __name__ == '__main__':
    # company = Company(
    #         name = "workiro",
    #         logo = "logo1.png",
    #         employee_count = "10",
    #         location = "Новосибирск",
    #         description = "Разрабатываем мобильные приложения и сервисы для сферы онлайн-обучения.",
    # )
    # company.save()
    # print(company)

    # company =  Company.objects.create(
    #     name="rebelrage",
    #     logo="logo2.png",
    #     employee_count="24",
    #     location="Москва",
    #     description="Мобильные сервисы, программное обеспечение, веб-сайты, мобильные приложения.",
    # )
    # print(company)