from django import forms
from .models import Project, TechStack, ContactInquiry, Testimony

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, React'}),
        }


class ProjectForm(forms.ModelForm):
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        # Use CheckboxSelectMultiple so multiple values can be posted as a list
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'tech-stack-checkboxes'}),
        required=True,
        label="Tech Stacks"
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project Description'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
        }


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your feedback/testimony here...'}),
        }
