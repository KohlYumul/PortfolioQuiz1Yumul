from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Project, PersonalInformation, ContactInquiry, Testimony
from .forms import ProjectForm, ContactInquiryForm, TestimonyForm

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


def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_project')
    else:
        form = ProjectForm()

    projects = Project.objects.all()
    return render(request, 'portfolio/add_project.html', {'form': form, 'projects': projects})


def contact_view(request):
    success_message = False
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = True
            form = ContactInquiryForm()
    else:
        form = ContactInquiryForm()

    personal_info = PersonalInformation.objects.first()
    context = {
        'info': personal_info,
        'form': form,
        'success': success_message
    }
    return render(request, 'portfolio/contact.html', context)


def add_testimony_view(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonies_list')
    else:
        form = TestimonyForm()
    return render(request, 'portfolio/add_testimony.html', {'form': form})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'portfolio/testimonies_list.html'
    context_object_name = 'testimonies'
    ordering = ['-created_at']


def testimony_detail_view(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'portfolio/testimony_detail.html', {'testimony': testimony})
