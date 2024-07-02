from django.contrib import admin
from .models import task_loader, sign_in
# Register your models here.

class task_loaderAdmin(admin.ModelAdmin):
    list_display = ('task_title','task_due_date',)

admin.site.register(task_loader, task_loaderAdmin)
admin.site.register(sign_in)