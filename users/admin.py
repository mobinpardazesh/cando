from django.contrib import admin
import home.models
from .models import User


# Register your models here.
@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user_name",)
