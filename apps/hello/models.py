from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_of_birth = models.DateField()
    bio = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    jabber = models.CharField(max_length=55)
    skype = models.CharField(max_length=55)
    other_contacts = models.CharField(max_length=255)
