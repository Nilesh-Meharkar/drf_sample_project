
from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ["id", "emp_id", "name", "city", "department"]



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["id", "dep_id", "name", "city", "specialization"]
