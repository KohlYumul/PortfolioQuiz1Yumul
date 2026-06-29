from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    my_info = {
        'email': 'kqyumul@student.hau.edu.ph',
        'location': 'Pampanga, Philippines',
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername',
    }
    return render(request, 'portfolio/contact.html', {'info': my_info})