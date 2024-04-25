from django import forms
from django.forms.utils import ValidationError
from portal.models import Financialyrtbl
from payments.models import Payments

month_val = [ 
    ('JANUARY','JANUARY'), ('FEBRUARY','FEBRUARY'),
    ('MARCH','MARCH'), ('APRIL','APRIL'),
    ('MAY','MAY'), ('JUNE','JUNE'),
    ('JULY','JULY'), ('AUGUST','AUGUST'),
    ('SEPTEMBER','SEPTEMBER'), ('OCTOBER','OCTOBER'),
    ('NOVEMBER','NOVEMBER'), ('DECEMBER','DECEMBER'),            
]

year_val = [ 
    ('2020','2020'), ('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024')
             
]

default_period = []
period_id = []

period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')
default_period = period_id

class LoanAppForm(forms.Form):
    '''member_id = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    loan_type = forms.CharField(max_length=20)'''
    loan_amount = forms.CharField(max_length=20)
    #year = forms.CharField(max_length=20, disabled = True)
    year = forms.CharField(max_length=20, widget=forms.Select(choices=year_val))
    month = forms.CharField(max_length=20, widget=forms.Select(choices=month_val))


class PaymentForm(forms.Form):
    class Meta:
        Model=Payments
        fields={'date','member_id','purpose','bank','transac_id','amount','evidence_file'}
    