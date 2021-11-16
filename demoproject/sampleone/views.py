from django.shortcuts import render
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import permissions


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        # List get
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Details individual get
        id=pk
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

    def create(self, request):
        # Post object
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        # Put update
        emp_id = pk
        stu = Employee.objects.get(pk=emp_id)
        serializer = EmployeeSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        # Patch update
        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)


    def destroy(self, request, pk):
        # Delete
        id = pk
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg': 'Data Deleted'})




class DepartmentViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        dep = Department.objects.all()
        serializer = DepartmentSerializer(dep, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Details individual get

        id = pk
        if id is not None:
            dep = Department.objects.get(id=id)
            serializer = DepartmentSerializer(dep)
            return Response(serializer.data)
