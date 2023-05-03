from django.db import models

company_status = (
    ('Active','Active'),
    ('Inactive','Inactive')
)

class acc_crt(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length = 12)
    # password = models.CharField(max_length=100)
    registerd = models.CharField(max_length=7)
    # club = models.CharField(max_length=100,default=True)
    # desc = models.TextField()
    date = models.TextField()

    def __str__(self):
        return self.name

class create_poc(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length = 12)
    company = models.CharField(max_length = 50)
    subdate = models.CharField(max_length = 12)
    status = models.CharField(max_length=100,choices = company_status)
    password = models.CharField(max_length=100)
    registerd = models.CharField(max_length=7)
    date = models.TextField()

    def __str__(self):
        return self.name


class details_comp(models.Model):
    
    details = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=10)
    package = models.CharField(max_length=10)
    branch = models.CharField(max_length=500)

    def __str__(self):
        return self.name
