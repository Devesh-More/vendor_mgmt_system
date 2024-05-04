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
<li>Open browser and put http://127.0.0.1:8000/admin/ in the url or after starting the server click on the link of started server as "control + click" on server link and add "/admin" next to the opened link in the browser.</li>
<li>Log in to django administrator using the credentials.</li>
<li>Create a token for token authentication</li>
<li>use the created token further</li>
<ul>

# API endpoint testings

<ul>
<h5>Postman Installations</h5>
<li>Click on the link https://www.postman.com/downloads/ to download the Postman.</li>
<li>Token Authentication: In the postman click on Headers and setup Authorization as key and Token your_token as value in the Headers.</li>
<h6>Getting all vendors details</h6>
<li>Setup GET request on the postman and hit the API endpoint http://127.0.0.1:8000/api/vendors</li>
<h6>Getting vendor with vendor-id</h6>
<li>Setup GET request on the postman and hit the API endpoint http://127.0.0.1:8000/api/vendors/id</li>
</ul>
<ul>
<h3>Vendor Creation</h3>
<li>Setup POST request on the postman and hit the API endpoint http://127.0.0.1:8000/api/vendors<br>
Use below JSON object to create a vendor:<br>
{
    "name": "vendor name",
    "contact_details": "contact details",
    "address": "address",
    "vendor_code": "vendor code",
    "on_time_delivery_rate": rate,
    "quality_rating_avg": quality_rating,
    "average_response_time": avg_resp_time,
    "fulfillment_rate": fulfillment_rate
}
</li>
</ul>
<h2>Vendor Details Update</h2>
<ul>
<li>Setup PUT or PATCH request on the postman and hit the API endpoint with id want to update using above JSON object http://127.0.0.1:8000/api/vendors/id
</li>
</ul>
<hr>
<h6>Getting all purchase order details</h6>
<li>Setup GET request on the postman and hit the API endpoint http://127.0.0.1:8000/api/purchase_order</li>
<h6>Getting purchase order with order-id</h6>
<li>Setup GET request on the postman and hit the API endpoint http://127.0.0.1:8000/api/purchase_order/id</li>
</ul>
<ul>
<h3>Purchase Order Creation</h3>
<li>Setup POST request on the postman and hit the API endpoint http://127.0.0.1:8000/api/purchase_order<br>
Use below JSON object to create a purchase order:<br>
{
    "po_number": "po_number",
    "order_date": "order_date",
    "delivery_date": "delivery_date",
    "items": [
        {
            "items": "number of items"
        }
    ],
    "quantity": numeric_quantity,
    "status": "pending",             eg:(completed,pending,canceled)
    "quality_rating": rating,
    "issue_date": "issue_date",
    "acknowledgment_date": "acknowledgment_date",
    "vendor": 4                      (Vendor id with it should be associated)
}
</li>
</ul>
<h2>Purchase Order Update</h2>
<ul>
<li>Setup PUT or PATCH request on the postman and hit the API endpoint with id want to update using above JSON object http://127.0.0.1:8000/api/purchase_order/id
</li>
</ul>
<hr>
