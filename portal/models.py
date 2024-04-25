# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Financialyrtbl(models.Model):
    periodid = models.CharField(db_column='PeriodID', primary_key=True,  max_length=4, null =False)  # Field name made lowercase.
    opendate = models.DateField(db_column='OpenDate', blank=True, null=True)  # Field name made lowercase.
    closedate = models.DateField(db_column='CloseDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=20, null=True)  # Field name made lowercase.
    currentlyused = models.CharField(db_column='CurrentlyUsed', max_length=20, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FinancialYrTbl'
    
    def __str__(self):
        return self.periodid





class Loansandpurchasestbl(models.Model):
    transactionid = models.IntegerField(db_column='TransactionID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    memberid = models.CharField(db_column='MemberID', max_length=20, null=True)  # Field name made lowercase.
    stationid = models.CharField(db_column='StationID', max_length=20)  # Field name made lowercase.
    sysdate = models.DateField(db_column='SysDate', blank=True, null=True)  # Field name made lowercase.
    enable = models.CharField(db_column='Enable', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    disable = models.CharField(db_column='Disable', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    accountname = models.CharField(db_column='AccountName', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    accountid = models.CharField(db_column='AccountID', max_length=20, null=True)  # Field name made lowercase.
    loantransacid = models.IntegerField(db_column='LoanTransacID', blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    firstintr = models.CharField(db_column='FirstIntr', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    subintr = models.CharField(db_column='SubIntr', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    subhead = models.CharField(db_column='SubHead', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    noofmonths = models.CharField(db_column='NoOfMonths', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    balbeforeinterest = models.CharField(db_column='BalBeforeInterest', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    installmentpay = models.CharField(db_column='InstallmentPay', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    medium = models.CharField(db_column='Medium', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    bank = models.CharField(db_column='Bank', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    auto = models.CharField(db_column='Auto', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    autointerest = models.CharField(db_column='AutoInterest', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    loanstatus = models.CharField(db_column='LoanStatus', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    interesttaken = models.CharField(db_column='InterestTaken', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    savingsaccount = models.CharField(db_column='SavingsAccount', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    interestrec = models.CharField(db_column='InterestRec', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    loantracidlink = models.CharField(db_column='LoanTracIDLink', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    datemodified = models.DateField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.
    currentlyserviced = models.CharField(db_column='CurrentlyServiced', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    voucherno = models.CharField(db_column='VoucherNo', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    adminchargeval = models.CharField(db_column='AdminChargeVal', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    details = models.CharField(db_column='Details', max_length=20, null=True)  # Field name made lowercase.
    periodid = models.CharField(db_column='PeriodID', max_length=20, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=20, null=True)  # Field name made lowercase.
    admchrgerec = models.CharField(db_column='AdmChrgeRec', max_length=20, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, null=True)  # Field name made lowercase.
    totalintrandprin = models.CharField(db_column='TotalIntrAndPrin', max_length=20, null=True)  # Field name made lowercase.
    originalprinamnt = models.CharField(db_column='OriginalPrinAmnt', max_length=20, null=True)  # Field name made lowercase.
    originalintramnt = models.CharField(db_column='OriginalIntrAmnt', max_length=20, null=True)  # Field name made lowercase.
    originaladmchrgeamnt = models.CharField(db_column='OriginalAdmChrgeAmnt', max_length=20, null=True)  # Field name made lowercase.
    originaltotalpayable = models.CharField(db_column='OriginalTotalPayable', max_length=20, null=True)  # Field name made lowercase.
    prinbal = models.CharField(db_column='PrinBal', max_length=20, null=True)  # Field name made lowercase.
    intrbal = models.CharField(db_column='IntrBal', max_length=20, null=True)  # Field name made lowercase.
    admchrgebal = models.CharField(db_column='AdmChrgeBal', max_length=20, null=True)  # Field name made lowercase.
    totalpayablebal = models.CharField(db_column='TotalPayableBal', max_length=20, null=True)  # Field name made lowercase.
    completed = models.CharField(db_column='Completed', max_length=20)  # Field name made lowercase.
    credit = models.TextField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    debit = models.TextField(db_column='Debit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoansAndPurchasesTbl'
        unique_together = (('loantransacid', 'periodid'),)

    def __str__(self):
        return self.accountname



class Memberaccounttypestbl(models.Model):
    accountcategory = models.TextField(db_column='AccountCategory', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    categorycode = models.CharField(db_column='CategoryCode', max_length=20, null=True)  # Field name made lowercase.
    accountid = models.CharField(db_column='AccountID', unique=True, max_length=20, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=20, null=True)  # Field name made lowercase. This field type is a guess.
    myorder = models.IntegerField(db_column='MyOrder', blank=True, null=True)  # Field name made lowercase.
    enable = models.TextField(db_column='Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disable = models.TextField(db_column='Disable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_credit_category = models.TextField(db_column='C_Credit_Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_credit_category_code = models.TextField(db_column='C_Credit_Category_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_credit_account = models.TextField(db_column='C_Credit_Account', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_credit_account_code = models.TextField(db_column='C_Credit_Account_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_debit_category = models.TextField(db_column='C_Debit_Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_debit_category_code = models.TextField(db_column='C_Debit_Category_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_debit_account = models.TextField(db_column='C_Debit_Account', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c_debit_account_code = models.TextField(db_column='C_Debit_Account_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_credit_category = models.TextField(db_column='D_Credit_Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_credit_category_code = models.TextField(db_column='D_Credit_Category_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_credit_account = models.TextField(db_column='D_Credit_Account', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_credit_account_code = models.TextField(db_column='D_Credit_Account_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_debit_category = models.TextField(db_column='D_Debit_Category', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_debit_category_code = models.TextField(db_column='D_Debit_Category_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_debit_account = models.TextField(db_column='D_Debit_Account', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d_debit_account_code = models.TextField(db_column='D_Debit_Account_Code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MemberAccountTypesTbl'
        unique_together = (('accountcategory', 'accountname'),)

    def __str__(self):
        return self.accountname



class Memberdatatbl(models.Model):
    memberid = models.CharField(db_column='MemberID', primary_key=True,unique=True, max_length=20)  # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datejoined = models.TextField(db_column='DateJoined', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sysdate = models.TextField(db_column='SysDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enable = models.TextField(db_column='Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disable = models.TextField(db_column='Disable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    names = models.TextField(db_column='Names', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    male = models.TextField(db_column='Male', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    female = models.TextField(db_column='Female', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    birthdate = models.TextField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.TextField(db_column='MaritalStatus', blank=True, null=True)  # Field name made lowercase.
    employstatus = models.TextField(db_column='EmployStatus', blank=True, null=True)  # Field name made lowercase.
    nationality = models.TextField(db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    lga = models.TextField(db_column='LGA', blank=True, null=True)  # Field name made lowercase.
    permadd = models.TextField(db_column='PermAdd', blank=True, null=True)  # Field name made lowercase.
    resadd = models.TextField(db_column='ResAdd', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.TextField(db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    designation = models.TextField(db_column='Designation', blank=True, null=True)  # Field name made lowercase.
    gradelevel = models.TextField(db_column='GradeLevel', blank=True, null=True)  # Field name made lowercase.
    scale = models.TextField(db_column='Scale', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.TextField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bank = models.TextField(db_column='Bank', blank=True, null=True)  # Field name made lowercase.
    accountno = models.TextField(db_column='AccountNo', blank=True, null=True)  # Field name made lowercase.
    sortcode = models.TextField(db_column='SortCode', blank=True, null=True)  # Field name made lowercase.
    savingspm = models.TextField(db_column='SavingsPM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstkinname = models.TextField(db_column='FirstKinName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstkinaddr = models.TextField(db_column='FirstKinAddr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstkinrelatnshp = models.TextField(db_column='FirstKinRelatnshp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstkinphoneno = models.TextField(db_column='FirstKinPhoneNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondkinname = models.TextField(db_column='SecondKinName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondkinaddr = models.TextField(db_column='SecondKinAddr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondkinrelatnshp = models.TextField(db_column='SecondKinRelatnshp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondkinphoneno = models.TextField(db_column='SecondKinPhoneNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    picloc = models.TextField(db_column='PicLoc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kinpicloc = models.TextField(db_column='KinPicLoc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    periodid = models.CharField(db_column='PeriodID', max_length=20, null=True)  # Field name made lowercase.
    smsalert = models.CharField(db_column='SmsAlert', max_length=20, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberDataTbl'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'




class Payorwithdrawtbl(models.Model):
    transactionid = models.IntegerField(db_column='TransactionID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    sysdate = models.DateField(db_column='SysDate', blank=True, null=True)  # Field name made lowercase.
    memberid = models.CharField(db_column='MemberID', max_length=20, null=True)  # Field name made lowercase.
    stationid = models.TextField(db_column='StationID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enable = models.TextField(db_column='Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disable = models.TextField(db_column='Disable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accountname = models.TextField(db_column='AccountName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accountid = models.TextField(db_column='AccountID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loantransacid = models.IntegerField(db_column='LoanTransacID',null=True)  # Field name made lowercase.
    amount = models.CharField(max_length=20, null=True)
    medium = models.TextField(db_column='Medium', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subhead = models.TextField(db_column='SubHead', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    recieptno = models.TextField(db_column='RecieptNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credit = models.TextField(db_column='Credit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    debit = models.TextField(db_column='Debit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bank = models.TextField(db_column='Bank', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    chequeno = models.TextField(db_column='ChequeNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    auto = models.TextField(db_column='Auto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    autointerest = models.TextField(db_column='AutoInterest', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    noofmonths = models.TextField(db_column='NoOfMonths', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    deposittransacid = models.CharField(db_column='DepositTransacID', max_length=20, null=True)  # Field name made lowercase.
    deposittransacidlink = models.CharField(db_column='DepositTransacIDLink', max_length=20, null=True)  # Field name made lowercase.
    depositinterestrec = models.CharField(db_column='DepositInterestRec', max_length=20, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=20, null=True)  # Field name made lowercase.
    interestpm = models.CharField(db_column='InterestPM', max_length=20, null=True)  # Field name made lowercase.
    interestval = models.CharField(db_column='Interestval', max_length=20, null=True)  # Field name made lowercase.
    periodid = models.CharField(db_column='PeriodID', max_length=20, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=20)  # Field name made lowercase.
    interestcomp = models.CharField(db_column='InterestComp', max_length=20, null=True)  # Field name made lowercase.
    admchrgecomp = models.CharField(db_column='AdmChrgeComp', max_length=20, null=True)  # Field name made lowercase.
    principalcomp = models.CharField(db_column='PrincipalComp', max_length=20, null=True)  # Field name made lowercase.
    loaninterestrec = models.CharField(db_column='LoanInterestRec', max_length=20, null=True)  # Field name made lowercase.
    admchrgerec = models.CharField(db_column='AdmChrgeRec', max_length=20, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, null=True)  # Field name made lowercase.
    loantracidlink = models.CharField(db_column='LoanTracIDLink', max_length=20,blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PayOrWithdrawTbl'
        unique_together = (('deposittransacid', 'periodid'),)


class Stationdb(models.Model):
    stationid = models.CharField(db_column='StationID', unique=True, max_length=20, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enablestation = models.TextField(db_column='EnableStation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disablestation = models.TextField(db_column='DisableStation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'StationDB'