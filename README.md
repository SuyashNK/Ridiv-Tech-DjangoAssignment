
# Invoice API README

 ## Overview
This API provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on Invoice and InvoiceDetail data using the Django REST Framework.

## Getting Started
**Prerequisites:**

* Python 3.x
* Django
* Django REST Framework

**Installation:**
git clone https://github.com/SuyashNK/Ridiv-Tech-DjangoAssignment

**Apply Database migrations:**
python manage.py migrate

**Run Development Server:**
python manage.py runserver

**Testing:**
python manage.py test invoices

### Additional information
**Models:**
* Invoice: Represents an invoice with a date, customer name, and related details.
* InvoiceDetail: Represents a specific detail within an invoice, including description, quantity, unit price, and total price.

### Contributing
* Fork the repository
* Create a branch for your changes
* Make your changes
* Submit a pull request