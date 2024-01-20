from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug')
    prepopulated_fields = {'slug':('category_name',)}

admin.site.register(Category,CategoryAdmin)