from django.db import models
from portal.models import Memberaccounttypestbl

# Create your models here.

month_val = [ 
    ('JANUARY','JANUARY'), ('FEBRUARY','FEBRUARY'),
    ('MARCH','MARCH'), ('APRIL','APRIL'),
    ('MAY','MAY'), ('JUNE','JUNE'),
    ('JULY','JULY'), ('AUGUST','AUGUST'),
    ('SEPTEMBER','SEPTEMBER'), ('OCTOBER','OCTOBER'),
    ('NOVEMBER','NOVEMBER'), ('DECEMBER','DECEMBER'),            
]


approval_val = [ 
    ('Yes','Approved'), ('No','Not Approved'),           
]

class LoanSetting(models.Model):
    loan_type = models.CharField('Loan Type', max_length=120)
    #loan_type = models.ForeignKey(Memberaccounttypestbl, on_delete=models.CASCADE, related_name='Loan')
    percentage_val = models.CharField(max_length=10)
    year_val = models.CharField('Year',max_length=4)
    month = models.CharField(max_length=50,choices=month_val)
    #event_date = models.DateTimeField('Event Date')
    max_loan_amnt = models.CharField('Max Loan Amount Available',max_length=120)
    #manager = models.CharField(max_length=60)
    #description = models.TextField(blank=True)

    def __str__(self):
        return self.year_val + "    " + self.month


class LoanApplication(models.Model):
    date = models.DateField(auto_now_add=True)
    member_id = models.CharField(max_length=10, blank=False)
    firstname = models.CharField('First Name',max_length=50, blank=False)
    lastname = models.CharField('Last Name',max_length=50, blank=False)
    loan_type = models.CharField('Loan Type', max_length=120)
    loan_amount = models.CharField('Loan Amount', max_length=120)
    year_val = models.CharField('Year',max_length=4)
    month = models.CharField(max_length=50,choices=month_val)
    
    loan_status = models.CharField('Approved?',max_length=10,choices=approval_val)


    def __str__(self):
        return self.month + "   " + self.member_id + "   " + self.loan_type + "   " + self.loan_amount + "   " + self.loan_status
