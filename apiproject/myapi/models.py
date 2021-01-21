from django.db import models

# Create your models here.

class ContaCorrente(models.Model):
    
    class Meta:
        db_table = "contacorrente"
    
    id = models.AutoField(primary_key=True)
    accountNumber = models.CharField(auto_created=True, max_length=100000, blank=False, unique= True)
    balance = models.DecimalField(default="0.00", decimal_places=2, max_digits=999999999999999)
    def __str__(self) -> str:
        return "Account: {} Balance: {} id: {}".format(self.accountNumber, self.balance,)