from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    employee_id = forms.CharField(widget=forms.TextInput(attrs={'class':'emp_class','id':'emp_id' ,'onfocusout':'copy()' }), help_text='Please enter your Employee Id')
    #is_employee = forms.BooleanField()
    member_id = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'mem_class','id':'mem_id'}), help_text='Required. 10 charaters of fewer.')
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','employee_id', 'member_id','email',)