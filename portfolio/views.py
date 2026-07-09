from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')


def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})


def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def contact_view(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'portfolio/contact.html', {'info': personal_info})
