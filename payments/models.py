from django.db import models

approval_val = [ 
    ('Yes','Approved'), ('No','Not Approved'),           
]

class Payments(models.Model):
    date = models.DateTimeField('Date Of Payment',auto_now_add=False)
    member_id = models.CharField(max_length=10, blank=False)
    purpose = models.CharField('Purpose Of Payment',max_length=50, blank=False)
    bank = models.CharField('Bank',max_length=50, blank=False)
    transac_id = models.CharField('Transac. ID/Teller No.', max_length=120)
    amount = models.CharField('Amount', max_length=120)
    
    confirmed = models.CharField('Confirmed?',max_length=10,choices=approval_val)
    evidence_file = models.FileField(upload_to='evidence_files/')

    def __str__(self):
        return self.member_id + "   " + self.bank + "   " + self.transac_id + "   " + self.amount
