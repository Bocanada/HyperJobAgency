from django.shortcuts import render
from django.views import View
from resume.models import Resume


# Create your views here.
class MainPage(View):
    paths = ['login', 'signup', 'vacancies', 'resumes', 'home']

    def get(self, request, *args, **kwargs):
        return render(request, 'resume/index.html', context={'paths': self.paths})


class ResumePage(View):
    resumes = Resume.objects

    def get(self, request, *args, **kwargs):
        return render(request, 'resume/resumes.html', context={'resumes': self.resumes.all()})
