from django.contrib import admin
from .models import Employee, Department
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id", "name"]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["dep_id", "name"]

