from django.contrib import admin
from .models import Project, PersonalInformation, ContactInquiry, Testimony

admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(ContactInquiry)
admin.site.register(Testimony)
