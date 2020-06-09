from django.shortcuts import render
from vacancy.models import Vacancy
from django.views import View
# Create your views here.

class VacancyPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})
