from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.generic import ListView
from .models import Project, TechStack, PersonalInformation, ContactInquiry, Testimony
from .forms import ProjectForm, TechStackForm, ContactInquiryForm, TestimonyForm, forms


# --- AUTHENTICATION GUARDFUNCTIONS ---
def is_superuser(user):
    return user.is_authenticated and user.is_superuser


# --- REQUIREMENT 1: SUPERUSER-ONLY SIGN-IN ---
def admin_login_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')

        user = authenticate(request, username=username_input, password=password_input)

        # Explicit check: User must be non-None AND a superuser/admin
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Access denied. Only superusers/admins can authenticate on this page.")

    return render(request, 'portfolio/admin_login.html')


def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')


# --- REQUIREMENT 2: DASHBOARD PAGE ---
@user_passes_test(is_superuser, login_url='admin_login')
def dashboard_view(request):
    projects = Project.objects.all().prefetch_related('tech_stacks')
    tech_stacks = TechStack.objects.all().prefetch_related('projects')

    context = {
        'projects': projects,
        'tech_stacks': tech_stacks,
    }
    return render(request, 'portfolio/dashboard.html', context)


# --- REQUIREMENT 3: CREATE PROJECT VIEW (RESTRICTED TO SUPERUSER) ---
@user_passes_test(is_superuser, login_url='admin_login')
def create_project_dashboard_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to create project. Please check the required fields.")
    else:
        form = ProjectForm()

    return render(request, 'portfolio/create_project.html', {'form': form})


# --- REQUIREMENT 3: CREATE TECH STACK VIEW (RESTRICTED TO SUPERUSER) ---
@user_passes_test(is_superuser, login_url='admin_login')
def create_tech_stack_dashboard_view(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tech stack created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Failed to create tech stack. Please check for duplicate names or empty inputs.")
    else:
        form = TechStackForm()

    return render(request, 'portfolio/create_tech_stack.html', {'form': form})


# --- PUBLIC PORTFOLIO VIEWS ---
def index(request):
    return render(request, 'portfolio/index.html')


def about(request):
    return render(request, 'portfolio/about.html')


def project_list_view(request):
    projects = Project.objects.all().prefetch_related('tech_stacks')
    return render(request, 'portfolio/projects_list.html', {'projects': projects})


def project_detail_view(request, pk):
    project = get_object_or_404(Project.objects.prefetch_related('tech_stacks'), pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


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
    return render(request, 'portfolio/contact.html', {'info': personal_info, 'form': form, 'success': success_message})


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
