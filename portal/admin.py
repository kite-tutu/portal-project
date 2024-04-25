from django.contrib import admin
import decimal
#import request as req
from django.contrib import admin
from portal.models import Loansandpurchasestbl,Financialyrtbl,Payorwithdrawtbl,Memberaccounttypestbl,Memberdatatbl

admin.site.site_header = 'Civil Servants MPCS Admin'
admin.site.site_title = 'Civil Servants MPCS Admin'
 
class MemberdatatblAdmin(admin.ModelAdmin):
    list_display = ['memberid', 'names', 'phoneno', 'smsalert']
    actions = ['send_account_balances']  # <-- Add the list action function here
    ordering = ['names']

    def send_account_balances(self, request, queryset):
        for member in queryset:
                ''' if member.smsalert == 'Yes':
                        member_id = member.memberid

                        period_id = []

                        member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=member_id).values("memberid","names","phoneno")
                                
                        period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')

                        accounts = Memberaccounttypestbl.objects.using('coopdb').all().values('accountcategory','accountname','myorder').order_by('myorder')
                        #print(f"{period_id}")
                        member_loans=[]

                        member_payments=[]

                        gen_transactions=[]

                        total_loan = 0
                        total_savings = 0
                        total_share = 0
                        grand_total = 0
                        
                        

                        member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
                        member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
                        transac_group = member_loans.union(member_payments, all=True).order_by('sysdate')

                        
                        account_balance_list = []
                        loan_sum = 0
                        savings_sum = 0 

                        for account in accounts:

                                        account_name = account['accountname']

                                        old_balance = 0
                                        last_payment = 0
                                        last_payment_date = ""
                                        account_balance = {}
                                        loan_id = '0'
                                        
                                        

                                        for transac in transac_group:

                                                if transac['accountname'] == account_name:

                                                        if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':
                                
                                                                #transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                                                                old_balance = transac['amount']

                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']

                                                                if int(loan_id) > 0:
                                                                        loan_sum = loan_sum + transac['amount']
                                                                else:
                                                                        savings_sum = savings_sum + transac['amount']

                                                                        account_balance.clear()
                                                                        account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id}
                                                        
                                                

                                                                        #new_transac_list.append(transac_rec)
                                                        
                                                        elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':

                                                                if transac['credit'] == 'Yes' and transac['loantransacid'] > 0:
                                                                        old_balance = old_balance - transac['amount']
                                                                        last_payment = transac['amount']
                                                                        last_payment_date = transac['sysdate']
                                                                        loan_id = transac['loantransacid']
                                                                        if int(loan_id) > 0:
                                                                                loan_sum = loan_sum - transac['amount']
                                                        elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                                                old_balance = old_balance + transac['amount']
                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']
                                                                savings_sum = savings_sum + transac['amount']
                                                        elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                                                old_balance = old_balance + transac['amount']
                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']
                                                                savings_sum = savings_sum + transac['amount']
                                                        elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                                                old_balance = old_balance + transac['amount']
                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']
                                                                if int(loan_id) > 0:
                                                                        loan_sum = loan_sum + transac['amount']
                                                        elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                                                old_balance = old_balance - transac['amount']
                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']
                                                                savings_sum = savings_sum - transac['amount']
                                                        elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                                                old_balance = old_balance - transac['amount']
                                                                last_payment = transac['amount']
                                                                last_payment_date = transac['sysdate']
                                                                loan_id = transac['loantransacid']
                                                                savings_sum = savings_sum - transac['amount']

                                                        account_balance.clear()
                                                        account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id}
                                                
                                                        account_balance_list.append(account_balance)
                                                        print (account_balance_list)


                                                        data = {'cmd': 'login','owneremail':'softwebsystems@yahoo.com',
                                                                'subacct':'landsmpcs@yahoo.com','subacctpwd':'landsandsurvey2019'
                                                        }
                                                        #http://www.smslive247.com/http/index.aspx?cmd=login&owneremail=xxx&subacct=xxx &subacctpwd=xxx

                                                        resp = request.POST("http://www.smslive247.com/http/index.aspx?", data={'cmd': 'login','owneremail':'softwebsystems@yahoo.com','subacct':'landsmpcs@yahoo.com','subacctpwd':'landsandsurvey2019'})
                                                        print(resp) 

                else:
                        pass '''
            
        #book.price = book.price * decimal.Decimal('0.9')
        #book.save()
        self.message_user(request, "Account Balances were succefully sent.")
    send_account_balances.short_description = 'Send Account Balances to Members'

admin.site.register(Memberdatatbl, MemberdatatblAdmin)