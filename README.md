# bloodbank-django-
This is a simple blood bank management system using Django (A python framework).

Technologies used here are:
* Backend: Python, Django
* Frontend: HTML, CSS, Javascript, BootStrap
* Database: SQLite
  

Short description:
-------------------

There are two sides at the application: Admin side and Donor side. 

* To be a donor, a person needs to tell the admin that he wants to be a donor.
Admin will take necessary information from the person and add him at the list of the donors.
Then, admin will provide a username and password for the new donor.

* After providing the correct username and password, the donor will be able to enter donor side.


At the donor side:
------------------

* Searching: An authenticated donor, can search for  available donors entering the blood group name and address.
The search can be done using only blood group name, only address , both blood group name and address.

A donor can't add, update or delete an donor.

He has the only permission to view the donors.


At the admin side:
-------------------

At the admin side, admin will be given the full permission over the system. 
Only admin can add, delete or update details of a donor.
             




