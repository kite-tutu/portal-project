
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from portal.models import Loansandpurchasestbl,Financialyrtbl,Payorwithdrawtbl,Memberaccounttypestbl,Memberdatatbl
from loans.models import LoanSetting,LoanApplication
from portal.forms import LoanAppForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import CustomUser

# Create your views here.
#

default_period = []
period_id = []

   

def dashboard(request):

   period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')
   default_period = period_id

   account_periods = Financialyrtbl.objects.using('coopdb').values('periodid','currentlyused').order_by('periodid')

   member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=request.user.member_id).values("memberid","names","phoneno")
       
   accounts = Memberaccounttypestbl.objects.using('coopdb').filter(enable='Yes').values('accountcategory','accountname','myorder').order_by('myorder')
   #print(f"{period_id}")
   member_loans=[]

   member_payments=[]

   gen_transactions=[]

   total_loan = 0
   total_savings = 0
   total_share = 0
   grand_total = 0
 
   

   member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
   member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
   
   ''' for index,amountval in member_payments:
         new_amount = amountval['amount']
         member_payments[index]['amount'] = str(new_amount) '''
      
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
            loan_id = 0
            
            

            for transac in transac_group:

                  if transac['accountname'] == account_name:

                        if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':
      
                              #transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                              old_balance = transac['amount']
                              if transac['credit'] == 'Yes':
                                    last_payment = transac['amount']
                                    last_payment_date = transac['sysdate']
                              loan_id = transac['loantransacid']
                              sub_head = transac['subhead']

                              if loan_id != 0:
                                    loan_sum = loan_sum + float(transac['amount'])
                              else:
                                    savings_sum = savings_sum + float(transac['amount'])

                              account_balance.clear()
                              account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id ,'sub_head':sub_head}
                              
                        

                              #new_transac_list.append(transac_rec)
                              
                        elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':
                              
                              loan_transac_type = type(transac['loantransacid'])
                              if loan_transac_type == int:
                                    if transac['credit'] == 'Yes' and transac['loantransacid'] != 0:
                                          old_balance = old_balance - float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          if loan_id != 0:
                                                loan_sum = loan_sum - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          if loan_id > 0:
                                                loan_sum = loan_sum + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])

                              elif loan_transac_type == str:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] == '0':
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])

                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])
                                    
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])

                        account_balance.clear()
                        account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id,'sub_head':sub_head}
                  
                        account_balance_list.append(account_balance)

                  else:
                        pass
                  

  # if net_total > 0 or net_total == 0:
  #    net_total_str = str(net_total)
  # elif net_total < 0:
  #    net_total_str = str(abs(net_total)

   #gen_transactions = member_loans.extends(member_payments)

   return render(request,'portal/dashboard.html',{'default_period':default_period,'period':period_id,'loan_sum':loan_sum,'savings_sum':savings_sum,'net_total':savings_sum - loan_sum,'account_balance_list':account_balance_list,'member_details':member_details,'account_periods':account_periods})

def dashboard_year(request,periodid):

   period_id = []
   period_id = periodid

   account_periods = Financialyrtbl.objects.using('coopdb').values('periodid','currentlyused').order_by('periodid')

   member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=request.user.member_id).values("memberid","names","phoneno")
       
   accounts = Memberaccounttypestbl.objects.using('coopdb').filter(enable='Yes').values('accountcategory','accountname','myorder').order_by('myorder')
   #print(f"{period_id}")
   member_loans=[]

   member_payments=[]

   gen_transactions=[]

   total_loan = 0
   total_savings = 0
   total_share = 0
   grand_total = 0
 
   

   member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
   member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
   
   ''' for index,amountval in member_payments:
         new_amount = amountval['amount']
         member_payments[index]['amount'] = str(new_amount) '''
      
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
            loan_id = 0
            
            

            for transac in transac_group:

                  if transac['accountname'] == account_name:

                        if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':
      
                              #transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                              old_balance = transac['amount']
                              if transac['credit'] == 'Yes':
                                    last_payment = transac['amount']
                                    last_payment_date = transac['sysdate']
                              loan_id = transac['loantransacid']
                              sub_head = transac['subhead']

                              if loan_id != 0:
                                    loan_sum = loan_sum + float(transac['amount'])
                              else:
                                    savings_sum = savings_sum + float(transac['amount'])

                              account_balance.clear()
                              account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id ,'sub_head':sub_head}
                              
                        

                              #new_transac_list.append(transac_rec)
                              
                        elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':
                              
                              loan_transac_type = type(transac['loantransacid'])
                              if loan_transac_type == int:
                                    if transac['credit'] == 'Yes' and transac['loantransacid'] != 0:
                                          old_balance = old_balance - float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          if loan_id != 0:
                                                loan_sum = loan_sum - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          if loan_id > 0:
                                                loan_sum = loan_sum + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])

                              elif loan_transac_type == str:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] == '0':
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])
                                    
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                          old_balance = old_balance + float(transac['amount'])
                                          if transac['credit'] == 'Yes':
                                                last_payment = float(transac['amount'])
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum + float(transac['amount'])

                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])
                                    
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                          old_balance = old_balance - float(transac['amount'])
                                          ''' last_payment = float(transac['amount'])
                                          last_payment_date = transac['sysdate'] '''
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']
                                          savings_sum = savings_sum - float(transac['amount'])

                        account_balance.clear()
                        account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id,'sub_head':sub_head}
                  
                        account_balance_list.append(account_balance)

                  else:
                        pass
                  

  # if net_total > 0 or net_total == 0:
  #    net_total_str = str(net_total)
  # elif net_total < 0:
  #    net_total_str = str(abs(net_total)

   #gen_transactions = member_loans.extends(member_payments)

   return render(request,'portal/dashboard.html',{'period':period_id,'loan_sum':loan_sum,'savings_sum':savings_sum,'net_total':savings_sum - loan_sum,'account_balance_list':account_balance_list,'member_details':member_details,'account_periods':account_periods})


def my_sort_func(my_col):
      return my_col['sysdate']


def transactions(request):
      period_id = []
      #all_periods = Financialyrtbl.objects.using('coopdb').get(status = 'Open')
      account_periods = Financialyrtbl.objects.using('coopdb').values('periodid','currentlyused').order_by('periodid')
      period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')
      member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=request.user.member_id).values("memberid","names","phoneno")
      #print(f"{period_id}")
      member_loans=[]
      member_loans2 =[]

      member_payments=[]

      transac_group = []

      balance = 0

      accounts = Memberaccounttypestbl.objects.using('coopdb').filter(enable='Yes').values('accountcategory','accountname','myorder').order_by('myorder')
      member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
      member_loans2 = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid","details")
      
      """ for loanrec in member_loans2:
            for memberloan in member_loans:
                  if loanrec['transactionid'] == memberloan['transactionid']:
                        details_rec = loanrec['details']
                        memberloan.update('subhead') = details_rec """

      member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
      transac_group = member_loans.union(member_payments, all=True).order_by('sysdate')


      #member_loans_sorted = member_loans.sort(key = my_sort_func)
      #member_payments_sorted = member_payments.sort(key = my_sort_func)

      #transac_group_sorted =  member_loans_sorted.union(member_payments_sorted, all=True)
      #num_of_transac = length(transac_group_sorted)

      new_transac_list = []
      sorted_transac_list = []

      for account in accounts:

            account_name = account['accountname']

            old_balance = 0

            for transac in transac_group:

                  if transac['accountname'] == account_name:

                        if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':

                              transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                              old_balance = float(transac['amount'])

                              new_transac_list.append(transac_rec)
                        
                        elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':
                              loan_transac_type = type(transac['loantransacid'])
                              if loan_transac_type == int:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] > 0:
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                          old_balance = old_balance - float(transac['amount'])
                                    
                              elif loan_transac_type == str:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] != '0':
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == '0':
                                          old_balance = old_balance + float(transac['amount']) 
                                    elif transac['credit'] == 'No' and transac['loantransacid'] != '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == '':  
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '':  
                                          old_balance = old_balance - float(transac['amount']) 
                              
                              transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':old_balance}
                              new_transac_list.append(transac_rec)

                  else:
                        pass

      #sorted_transac_list = new_transac_list.sort(key=my_sort_func)

      return render(request,'portal/transactions.html',{'accounts':accounts,'member_loans':member_loans,'member_payments':member_payments,'transac_group':transac_group,'balance':0,'new_transac_list':new_transac_list,'sorted_transac_list':sorted_transac_list,'member_details':member_details,'account_periods':account_periods})


def transactions_year(request,periodid):
      period_id = periodid

      account_periods = Financialyrtbl.objects.using('coopdb').values('periodid','currentlyused').order_by('periodid') 
      #period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')
      member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=request.user.member_id).values("memberid","names","phoneno")
      #print(f"{period_id}")
      member_loans=[]
      member_loans2 =[]

      member_payments=[]

      transac_group = []

      balance = 0

      accounts = Memberaccounttypestbl.objects.using('coopdb').filter(enable='Yes').values('accountcategory','accountname','myorder').order_by('myorder')
      member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
      member_loans2 = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid","details")
      
      """ for loanrec in member_loans2:
            for memberloan in member_loans:
                  if loanrec['transactionid'] == memberloan['transactionid']:
                        details_rec = loanrec['details']
                        memberloan.update('subhead') = details_rec """

      member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
      transac_group = member_loans.union(member_payments, all=True).order_by('sysdate')


      #member_loans_sorted = member_loans.sort(key = my_sort_func)
      #member_payments_sorted = member_payments.sort(key = my_sort_func)

      #transac_group_sorted =  member_loans_sorted.union(member_payments_sorted, all=True)
      #num_of_transac = length(transac_group_sorted)

      new_transac_list = []
      sorted_transac_list = []

      for account in accounts:

            account_name = account['accountname']

            old_balance = 0

            for transac in transac_group:

                  if transac['accountname'] == account_name:

                        if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':

                              transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                              old_balance = float(transac['amount'])

                              new_transac_list.append(transac_rec)
                        
                        elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':
                              loan_transac_type = type(transac['loantransacid'])
                              if loan_transac_type == int:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] > 0:
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                          old_balance = old_balance - float(transac['amount'])
                                    
                              elif loan_transac_type == str:

                                    if transac['credit'] == 'Yes' and transac['loantransacid'] != '0':
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == '0':
                                          old_balance = old_balance + float(transac['amount']) 
                                    elif transac['credit'] == 'No' and transac['loantransacid'] != '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '0':  
                                          old_balance = old_balance - float(transac['amount'])
                                    elif transac['credit'] == 'Yes' and transac['loantransacid'] == '':  
                                          old_balance = old_balance + float(transac['amount'])
                                    elif transac['credit'] == 'No' and transac['loantransacid'] == '':  
                                          old_balance = old_balance - float(transac['amount']) 
                              
                              transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':old_balance}
                              new_transac_list.append(transac_rec)

                  else:
                        pass

      #sorted_transac_list = new_transac_list.sort(key=my_sort_func)

      return render(request,'portal/transactions.html',{'period':period_id,'accounts':accounts,'member_loans':member_loans,'member_payments':member_payments,'transac_group':transac_group,'balance':0,'new_transac_list':new_transac_list,'sorted_transac_list':sorted_transac_list,'member_details':member_details,'account_periods':account_periods})

''' def account_details(request,name):
   account_name = request.POST.get('name')

   period_id = []
       
   period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')

   #print(f"{period_id}")
   member_loans=[]

   member_payments=[]

   acct_category = Memberaccounttypestbl.objects.using('coopdb').get(accountname = account_name )
   category_val = acct_category.accountcategory

   if category_val == 'Purchases':
         member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,accountname = account_name ).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
         member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Purchases',accountname = account_name).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")  
         transac_group = member_loans.union(member_payments, all=True)
   elif category_val == 'Loans':
         member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,accountname = account_name ).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
         member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Loans',accountname = account_name).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")  
         transac_group = member_loans.union(member_payments, all=True)
   elif category_val == 'Savings':
         member_loans = []#Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Savings',accountname = account_name ).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
         member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Savings',accountname = account_name).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")  
         transac_group = member_loans.union(member_payments, all=True)
   elif category_val == 'Share-Capital':
         member_loans = []#Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Savings',accountname = account_name ).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
         member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id,category='Share-Capital',accountname = account_name).value_list("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")  
         transac_group = member_loans.union(member_payments, all=True)
   return HttpResponse(transac_group)
   #return render(request,'portal/transactions.html',{'transac_group':transac_group}) '''

def loanapplication(request):

      period_id = []
      all_loan_applications=[]

      period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')
      default_period = period_id
      
      if request.method == 'POST':

            user_instance = get_object_or_404(CustomUser,member_id=request.user.member_id)
            loan_instance = LoanApplication()
            form = LoanAppForm(request.POST,initial={"year":default_period})
            total_sofar = 0.0

            if form.is_valid():
                  # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                  #book_instance.due_back = form.cleaned_data['renewal_date']
                  #book_instance.save()

                  loan_instance.member_id = user_instance.member_id
                  loan_instance.firstname =  user_instance.first_name
                  loan_instance.lastname = user_instance.last_name
                  loan_instance.loan_type = "COOP LOAN"
                  loan_instance.loan_amount = form.cleaned_data['loan_amount']
                  loan_instance.year_val = form.cleaned_data['year']
                  loan_instance.month = form.cleaned_data['month']
                  loan_instance.loan_status = "Approved"


                  member_details = Memberdatatbl.objects.using('coopdb').filter(memberid=request.user.member_id).values("memberid","names","phoneno")
                        
                 # period_id = Financialyrtbl.objects.using('coopdb').get(currentlyused = 'Yes')

                  accounts = Memberaccounttypestbl.objects.using('coopdb').filter(enable='Yes').values('accountcategory','accountname','myorder').order_by('myorder')
                  #print(f"{period_id}")
                  member_loans=[]

                  member_payments=[]

                  gen_transactions=[]

                  total_loan = 0
                  total_savings = 0
                  total_share = 0
                  grand_total = 0
                  
                  

                  member_loans = Loansandpurchasestbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
                  member_payments = Payorwithdrawtbl.objects.using('coopdb').filter(memberid=request.user.member_id, periodid=period_id).values("transactionid","sysdate","memberid","stationid","enable","disable","accountname","accountid","loantransacid","credit","debit","amount","subhead","loantracidlink","periodid")
                  
                  ''' for index,amountval in member_payments:
                        new_amount = amountval['amount']
                        member_payments[index]['amount'] = str(new_amount) '''
                        
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
                        loan_id = 0
                        
                        

                        for transac in transac_group:

                              if transac['accountname'] == account_name:

                                    if transac['accountname'] == account_name and  transac['subhead'] == 'Opening Balance':
                  
                                          #transac_rec = { 'transactionid':transac['transactionid'],'sysdate':transac['sysdate'],'memberid':transac['memberid'],'stationid':transac['stationid'],'enable':transac['enable'],'disable':transac['disable'],'accountname':transac['accountname'],'accountid':transac['accountid'],'loantransacid':transac['loantransacid'],'credit':transac['credit'],'debit':transac['debit'],'amount':transac['amount'],'subhead':transac['subhead'],'loantracidlink':transac['loantracidlink'],'periodid':transac['periodid'],'balance':transac['amount']}

                                          old_balance = transac['amount']
                                          if transac['credit'] == 'Yes':
                                                last_payment = transac['amount']
                                                last_payment_date = transac['sysdate']
                                          loan_id = transac['loantransacid']
                                          sub_head = transac['subhead']

                                          if loan_id != 0:
                                                loan_sum = loan_sum + float(transac['amount'])
                                          else:
                                                savings_sum = savings_sum + float(transac['amount'])

                                          account_balance.clear()
                                          account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id ,'sub_head':sub_head}
                                          
                                    

                                          #new_transac_list.append(transac_rec)
                                          
                                    elif transac['accountname'] == account_name and transac['subhead'] != 'Opening Balance':
                                          
                                          loan_transac_type = type(transac['loantransacid'])
                                          if loan_transac_type == int:
                                                if transac['credit'] == 'Yes' and transac['loantransacid'] != 0:
                                                      old_balance = old_balance - float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      if loan_id != 0:
                                                            loan_sum = loan_sum - float(transac['amount'])
                                                elif transac['credit'] == 'Yes' and transac['loantransacid'] == 0:
                                                      old_balance = old_balance + float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum + float(transac['amount'])
                                                elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                                      old_balance = old_balance + float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum + float(transac['amount'])
                                                elif transac['credit'] == 'No' and transac['loantransacid'] > 0:  
                                                      old_balance = old_balance + float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      if loan_id > 0:
                                                            loan_sum = loan_sum + float(transac['amount'])
                                                elif transac['credit'] == 'No' and transac['loantransacid'] == 0:  
                                                      old_balance = old_balance - float(transac['amount'])
                                                      ''' last_payment = float(transac['amount'])
                                                      last_payment_date = transac['sysdate'] '''
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum - float(transac['amount'])
                                                elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                                      old_balance = old_balance - float(transac['amount'])
                                                      ''' last_payment = float(transac['amount'])
                                                      last_payment_date = transac['sysdate'] '''
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum - float(transac['amount'])

                                          elif loan_transac_type == str:

                                                if transac['credit'] == 'Yes' and transac['loantransacid'] == '0':
                                                      old_balance = old_balance + float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum + float(transac['amount'])
                                                
                                                elif transac['credit'] == 'Yes' and transac['loantransacid'] == "":
                                                      old_balance = old_balance + float(transac['amount'])
                                                      if transac['credit'] == 'Yes':
                                                            last_payment = float(transac['amount'])
                                                            last_payment_date = transac['sysdate']
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum + float(transac['amount'])

                                                elif transac['credit'] == 'No' and transac['loantransacid'] == '0':  
                                                      old_balance = old_balance - float(transac['amount'])
                                                      ''' last_payment = float(transac['amount'])
                                                      last_payment_date = transac['sysdate'] '''
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum - float(transac['amount'])
                                                
                                                elif transac['credit'] == 'No' and transac['loantransacid'] == "":  
                                                      old_balance = old_balance - float(transac['amount'])
                                                      ''' last_payment = float(transac['amount'])
                                                      last_payment_date = transac['sysdate'] '''
                                                      loan_id = transac['loantransacid']
                                                      sub_head = transac['subhead']
                                                      savings_sum = savings_sum - float(transac['amount'])

                                    account_balance.clear()
                                    account_balance = { 'account_name':account_name,'amount':old_balance,'last_payment':last_payment,'last_payment_date':last_payment_date,'loan_id':loan_id,'sub_head':sub_head}
                              
                                    account_balance_list.append(account_balance)
                  avail_amount=[]
                  bal_available = 0
                  total_balance = 0
                  avail_amnt_val = 0
                  avail_amount = LoanSetting.objects.using('default').filter(year_val=loan_instance.year_val,month=loan_instance.month).values("year_val","month","max_loan_amnt")
                  
                  avail_amnt_val = float(avail_amount[0]['max_loan_amnt'])
                  if avail_amount[0]['max_loan_amnt'] == "":
                        avail_amnt_val = 0
                  approved_applications = LoanApplication.objects.using('default').filter(year_val=default_period,month=loan_instance.month).values("loan_amount")
                  print(approved_applications)
                  print(avail_amount)

                  for loanamnt in approved_applications:
                        total_sofar = total_sofar + float(loanamnt['loan_amount'])
                  print(total_sofar)

                  for amount_val_avail in avail_amount:
                        total_balance = amount_val_avail['max_loan_amnt']

                  bal_available = float(total_balance) - total_sofar

                  
                  if float(loan_instance.loan_amount) > 3 * savings_sum:
                        messages.info(request, f'The Loan amount exceeds three times your total asset,enter for a lower amount')
                        print(approved_applications)
                        print(avail_amount)
                  elif loan_sum > 0:
                        messages.info(request, f'You have a running loan balance hence you are not eligible for a new loan now')
                  elif float(loan_instance.loan_amount) > bal_available and bal_available == 0 :
                        messages.info(request, f'The limit for the month has been reached, please apply for the next month')
                  elif float(loan_instance.loan_amount) > bal_available and bal_available != 0 :
                        messages.info(request, f"The balance '('%s')' for the month cannot accomodate your request. You may apply for the available amount or schedule your requested amount for next month" %bal_available)
                  elif (float(loan_instance.loan_amount) <= 3 * savings_sum and loan_sum <= 0 and float(loan_instance.loan_amount) <= avail_amnt_val):
                        existing_application = LoanApplication.objects.using('default').filter(member_id=request.user.member_id, year_val=loan_instance.year_val,month=loan_instance.month).values("year_val","month","member_id")
                        if existing_application:
                              messages.info(request, f'You already have a pending application for this month')
                        else:
                              loan_instance.save()
                              messages.success(request, f'Congratulations! Your loan application was successful.')
                  else:
                        all_loan_applications = LoanApplication.objects.using('default').filter(member_id=request.user.member_id).values("year_val","month","member_id","date","loan_type","loan_amount")
                        form = LoanAppForm(initial={"year":default_period})
                        #return render(request,'portal/loanapplication.html',{'form':form,'year_val':default_period,'loan_applications':all_loan_applications})
                  # redirect to a new URL:
                  #return HttpResponseRedirect(reverse('all-borrowed') )
                  #pass

      else:
                  
                  all_loan_applications = LoanApplication.objects.using('default').filter(member_id=request.user.member_id).values("year_val","month","member_id","date","loan_type","loan_amount","loan_status")
                  form = LoanAppForm(initial={"year":default_period,'loan_applications':all_loan_applications})
      return render(request,'portal/loanapplication.html',{'form':form,'year_val':default_period,'loan_applications':all_loan_applications})
      #return render(request,'portal/loanapplication.html',{'period':period_id,'loan_sum':loan_sum,'savings_sum':savings_sum,'net_total':savings_sum - loan_sum,'account_balance_list':account_balance_list,'member_details':member_details,'form':form})

def payments(request):
      pass

def shopindex(request):
       
      return render(request, 'portal/shopindex.html')

def categories(request):
      return render(request, 'portal/categories.html')
