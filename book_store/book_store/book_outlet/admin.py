from django.contrib import admin

from .models import book, author_name, address, country

# Register your models here.


class bookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'sluged_url':('title',)}
    list_display = ('title','author',)
    list_filter = ('rating',)


admin.site.register(book, bookAdmin)
admin.site.register(author_name)
admin.site.register(address)
admin.site.register(country)