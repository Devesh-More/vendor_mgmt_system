<h1>Project creation and setup description</h1>

# vendor_mgmt_system

<h5>Objective<h5>
Vendor Management System has used Django and Django REST Framework. This system handles vendor profiles, track purchase orders, and calculates vendor performance metrics.

# Technologies Used

<ul>
<li>Python 3.11.2</li>
<li>Django</li>
<li>Django REST Framework</li>
</ul>

# Setup

<h5>Create Python Virtual Environment</h5>
<h6>venv create command</h6>
<ul>
<li> python -m venv "environment name"</li>
</ul>
<h6>venv activation command</h6>
<ul>
<li> Windows: environment name/Scripts/activate </li>
<li> OSX: source environment name/bin/activate </li>
</ul>

# Python Required Packages Installation

<ul>
<li>pip install Django</li>
<li>pip install djangorestframework</li>
</ul>

# Create django project

<h6>Project and app start command</h6>
<ul>
<li>django-admin startproject Vendor</li>
<li> cd Vendor </li>  (Navigate to Project directory )
<li>python manage.py startapp VendorApp</li>
</ul>

# Model (Database) creation

<ul>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
</ul>

# Superuser Creation

<h6>Commands</h6>
<ul>
<li>python manage.py createsuperuser</li>
</ul>

# Start Server

<ul><li>python manage.py runserver</li></ul>

# Django Administrator and Token creation

<ul>
<li>Open browser and put http://127.0.0.1:8000/admin/ in the url or after starting the server click on the link of started server as "control + click" on server link and add /admin next to the opened link on browser.</li>
<li>Log in to django administrator using the credentials.</li>
<li>Create a token for token authentication</li>
<li>use the created token further</li>
<ul>

# Vendor Creation
