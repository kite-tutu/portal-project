from django.contrib import admin
from payments.models import Payments

class PaymentsAdmin(admin.ModelAdmin):

    list_display = ['date','member_id','bank','transac_id','amount', 'confirmed']
    #actions = ['send_account_balances']  # <-- Add the list action function here
    ordering = ['date']
    search_fields = (
    'date','member_id',
)

admin.site.register(Payments, PaymentsAdmin)