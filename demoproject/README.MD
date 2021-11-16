

## Install Django and Django REST framework into the virtual environment
>> pip install django
>> pip install djangorestframework

# Set up a new project with a "sampleone" application
>> django-admin startproject demoproject
>> cd demoproject
>> django-admin startapp sampleone




## Add 'rest_framework' & 'sampleone' in settings 'INSTALLED_APPS'

>>INSTALLED_APPS =    
	[	...
		'rest_framework',
		'sampleone',
	]
	
	
	
	
# Added employee models.
	
	
	
>> python manage.py migrate
>> python manage.py makemigrations


# create super user
>> python manage.py createsuperuser

	username: admin
	email: admin@admin.com
	password: admin
	
	