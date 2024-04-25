from django.db import models
from django.contrib.auth.models import AbstractUser

    


class CustomUser(AbstractUser):
    employee_id = models.CharField(max_length=20, blank=True)
    member_id = models.CharField(max_length=10, blank=False)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self):
        if self.first_name != "" and self.last_name != "":
            if str(self.is_active):
                return self.first_name + " " + self.last_name + " (Active User)"
            else:
                return self.first_name + " " + self.last_name + " (Inactive User)" 
        else:
            return self.username

