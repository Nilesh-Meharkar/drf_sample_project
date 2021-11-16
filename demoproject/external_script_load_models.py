import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'demoproject.settings'
application = get_wsgi_application()

# Importing django resources after loading the settings file
from sampleone.models import Employee, Department


emp_data = [
    {
        "emp_id": 1,
        "name": "sam",
        "city": "Pune",
        "department": "Physics"
    },

    {
        "emp_id": 5,
        "name": "Ram",
        "city": "Delhi",
        "department": "Maintenance"
    },
]


dep_data = [
    {
        "dep_id": 34,
        "name": "Riya",
        "city": "Pune",
        "specialization": "Computer"
    }

]


for data in emp_data:
    emp = Employee()
    emp.emp_id = data["emp_id"]
    emp.name = data["name"]
    emp.city = data["city"]
    emp.department = data["department"]
    emp.save()

for data in dep_data:
    dep = Department()
    dep.dep_id = data["dep_id"]
    dep.name = data["name"]
    dep.city = data["city"]
    dep.specialization = data["specialization"]
    dep.save()