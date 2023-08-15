from django.contrib import admin
import home.models


# Register your models here.
@admin.register(home.models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
    "student_name", "student_familly", "student_Age", "student_fathername","student_username", "student_email")
