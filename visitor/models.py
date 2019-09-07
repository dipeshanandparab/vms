from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    visit_date = models.DateTimeField('visit_date')

    def __str__(self):
        return self.visitor_name


