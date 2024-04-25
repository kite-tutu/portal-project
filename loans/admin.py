from django.contrib import admin
from loans.models import LoanSetting,LoanApplication
#import request as req

# Register your models here.

class LoansAdmin(admin.ModelAdmin):

    list_display = ['year_val','month', 'member_id','firstname','lastname','loan_type', 'loan_amount','loan_status','date']
    #actions = ['send_account_balances']  # <-- Add the list action function here
    ordering = ['date']
    search_fields = (
    'year_val','month',
)

admin.site.register(LoanSetting)
admin.site.register(LoanApplication, LoansAdmin)
