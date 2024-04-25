from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):

    #list_display = ['year_val','month', 'member_id','firstname','lastname','loan_type', 'loan_amount','loan_status','date']
    #actions = ['send_account_balances']  # <-- Add the list action function here
    #ordering = ['date']
    search_fields = (
    'first_name','last_name',
)
admin.site.register(CustomUser,CustomUserAdmin)


