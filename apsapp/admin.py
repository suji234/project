from django.contrib import admin

from .models import Admin,Customer,Patient,Feedback

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Patient)
admin.site.register(Feedback)